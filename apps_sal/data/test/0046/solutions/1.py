#!/usr/bin/env python3

try:
    while True:
        n, m = list(map(int, input().split()))
        a = [0] * 5
        b = [0] * 5
        for i in range(1, n + 1):
            a[i % 5] += 1
        for j in range(1, m + 1):
            b[j % 5] += 1

        print(a[0] * b[0] + a[1] * b[4] + a[2] * b[3] + a[3] * b[2] + a[4] * b[1])

except EOFError:
    pass
