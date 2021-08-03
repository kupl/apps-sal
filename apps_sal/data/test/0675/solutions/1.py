import sys
import math

m, t, r = map(int, input().split())

if r > t:
    print(-1)
    return

candles = []
gh = list(map(int, input().split()))

for i in range(m):
    g = gh[i]
    now_on = 0
    for c in candles:
        if g - c <= t:
            now_on += 1

    for k in range(r - now_on):
        candles.append(g - 1 - k)

print(len(candles))
