#!/usr/bin/env python3

a = list(map(int, input().split()))[1]
b = list(map(int, input().split()))

try_ = -1
c = 0
s = 0

for i in range(len(b) - 1):
    if b[i+1] - b[i] > a:
        s = -10e5

while b[try_] != b[c]:
    if b[try_] - b[c] <= a:
        s += 1
        c = try_
        try_ = -1
    else:
        try_ -= 1

print(s if s > 0 else -1)

