import sys


def print_list(list):
    for i in list:
        print(i, end=" ")
    print()


n, k = [int(i) for i in input().split(" ")]
my_list = [int(i) for i in input().split(" ")]

stack = list()

next_pop = 1

for num in my_list:
    if stack and stack[-1] < num:
        print("-1")
        return

    stack.append(num)

    while stack and stack[-1] == next_pop:
        stack.pop()
        next_pop += 1

while stack:
    for i in range(stack[-1] - 1, next_pop - 1, -1):
        my_list.append(i)
    next_pop = stack.pop() + 1

if next_pop > n:
    print_list(my_list)
else:
    for j in range(n, next_pop - 1, -1):
        my_list.append(j)
    print_list(my_list)
