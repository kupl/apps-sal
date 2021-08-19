#!/usr/bin/env python3

n, a, b = [int(x) for x in input().split()]

if n > a * b:
    print(-1)
else:
    for i in range(0, a):
        if i % 2 == 0:
            for j in range(b * i, b * (i + 1)):
                if j >= n:
                    print(0, end=' ')
                else:
                    print(j + 1, end=' ')
        else:
            for j in range(b * (i + 1) - 1, b * i - 1, -1):
                if j >= n:
                    print(0, end=' ')
                else:
                    print(j + 1, end=' ')
        print()
