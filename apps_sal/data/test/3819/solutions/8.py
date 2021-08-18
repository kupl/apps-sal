import io
import os

n = int(input())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

f = True
if 1 in b:

    j = b.index(1)

    for i in range(n - j):
        d = i + 1 - b[j + i]
        if d != 0:
            break
    else:
        s = -2
        for k in range(j):
            if b[k] != 0 and b[k] - k <= n - (j - 1):
                break
        else:
            print(j)
            f = False


if f:
    s = -2
    for k in range(n):
        if b[k] != 0:
            s = max(s, k - b[k])
    print(s + n + 2)
