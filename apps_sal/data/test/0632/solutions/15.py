import math
import sys
t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    for i in range(k):
        if n % 2 == 0:
            n += 2 * (k - i)
            break
        else:
            for d in range(3, 1000, 2):
                if n % d == 0 or d * d > n:
                    break
            if n % d > 0:
                d = n
            n += d
    print(n)
