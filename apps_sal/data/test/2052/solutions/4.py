#!/usr/bin/env python3

[w, l] = list(map(int, input().strip().split()))
ais = list(map(int, input().strip().split()))

winais = [0 for _ in range(w - l)]
s = sum(ais[:l])
winais[0] = s
for i in range(w - l - 1):
    s += ais[i + l] - ais[i]
    winais[i + 1] = s

print(min(winais))
