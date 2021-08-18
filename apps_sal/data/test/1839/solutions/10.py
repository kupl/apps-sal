import sys


n = int(input())

vert = [False for i in range(n)]
gor = [False for i in range(n)]

for i in range(n ** 2):
    x, y = [int(i) - 1 for i in input().split()]
    if not vert[x] and not gor[y]:
        vert[x] = True
        gor[y] = True
        print(i + 1, end=' ')

print()
