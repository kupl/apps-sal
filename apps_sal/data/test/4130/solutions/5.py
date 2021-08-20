import math
n = int(input())
list1 = input().split()
for i in range(n):
    list1[i] = int(list1[i])
list1.sort()
for i in range(n):
    if i == 0:
        if list1[i] > 1:
            list1[i] -= 1
    elif list1[i] < list1[i - 1]:
        list1[i] += 1
    elif list1[i] == list1[i - 1]:
        list1[i] += 1
    elif list1[i] > list1[i - 1] + 1:
        list1[i] -= 1
list1.sort()
num = 0
curr = 0
for i in range(n):
    if list1[i] != curr:
        num += 1
        curr = list1[i]
print(num)
