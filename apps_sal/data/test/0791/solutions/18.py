import math

n = int(input())
str = input()

res = ['' for i in range(n)]
b = True
for i in range(n):
    if str[i] == '0':
        res[i] = '1'
        for j in range(i):
            res[j] = '0'
        b = False

        for j in range(i+1, n):
            res[j] = str[j]

        break


if b:
    print(n)
else:
    total = 0
    for i in range(n):
        if res[i]!=str[i]:
            total+=1
    print(total)
