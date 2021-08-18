#!/usr/bin/env python3
from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n, m = rint()

a = list(rint())
b = list(rint())

ans = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    if i != n - 1:
        for j in range(m - 1):
            ans[i][j] = 0
        ans[i][m - 1] = a[i]
    else:
        for j in range(m - 1):
            ans[i][j] = b[j]
        row_xor = 0
        for j in range(m - 1):
            row_xor = row_xor ^ ans[i][j]
        col_xor = 0
        for j in range(n - 1):
            col_xor = col_xor ^ ans[j][m - 1]
        if row_xor ^ a[n - 1] == col_xor ^ b[m - 1]:
            ans[i][m - 1] = row_xor ^ a[n - 1]
        else:
            print("NO")
            return

print("YES")
for i in range(n):
    print(*ans[i])
