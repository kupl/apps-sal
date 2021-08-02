'''input
6
5 4 5 4 4 5
'''
from sys import stdin


def check_valid(string):
    stack = []
    for i in string:
        if i in ['(', '[']:
            stack.append(i)
        elif i == ')':
            if len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop()
                    continue
            return False
        elif i == ']':
            if len(stack) > 0:
                if stack[-1] == '[':
                    stack.pop()
                    continue
            return False

    return len(stack) == 0


def merge(index):
    aux = []
    if len(index) > 0:
        aux = [index[0]]
        for i in range(1, len(index)):
            if index[i][0] == aux[-1][1] + 1:
                aux[-1][1] = index[i][1]
            else:
                if check_valid(string[aux[-1][1] + 1: index[i][0]]):
                    aux[-1][1] = index[i][1]
                else:
                    aux.append(index[i])
    return aux


# main starts
n = int(stdin.readline().strip())
arr = []
arr = list(map(int, stdin.readline().split()))
for i in range(n):
    arr[i] = [i, arr[i]]

arr.sort(key=lambda x: x[1], reverse=True)
count = 0
ans = []
total = 0
for i in range(n):
    index, a = arr[i]
    ans.append(index + 1)
    total += count * a + 1

    count += 1

print(total)
print(*ans)
