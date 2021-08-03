#!/usr/bin/env python3

try:
    while True:
        n = int(input())
        s = input()
        a = list(map(int, input().split()))
        result = -1
        for i in range(1, n):
            if s[i - 1] == 'R' != s[i]:
                t = (a[i] - a[i - 1]) >> 1
                if result == -1 or t < result:
                    result = t
        print(result)

except EOFError:
    pass
