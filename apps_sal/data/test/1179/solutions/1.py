#!/usr/bin/env python3

try:
    while True:
        n, k = list(map(int, input().split()))
        a = list(map(int, input().split()))
        for i in range(1, n + 1):
            if k <= i:
                print(a[k - 1])
                break

            k -= i

except EOFError:
    pass

