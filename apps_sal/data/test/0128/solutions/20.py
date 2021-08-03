#!/usr/bin/env python3

n, k = [int(x) for x in input().split()]

# 1 2 3 4 5
# 5 2 3 4 1

if n == 1:
    print(0)
else:
    result = 0
    l = n
    for i in range(0, min(n // 2, k)):
        result += (l - 1) + (l - 2)
        l -= 2
    print(result)
