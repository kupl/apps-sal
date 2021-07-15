#!/usr/env python3

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input())
for i in range(n):
    for j in range(m):
        if i % 2:
            if j % 2 and a[i][j] == '.':
                print('B', end='')
            elif a[i][j] == '.':
                print('W', end='')
            else:
                print('-', end='')
        else:
            if a[i][j] == '.' and j % 2:
                print('W', end='')
            elif a[i][j] == '.':
                print('B', end='')
            else:
                print('-', end='')
    print()

