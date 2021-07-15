#!/usr/bin/env python3
N, *AB = list(map(int, open(0).read().split()))
AB_sorted = sorted(zip(AB[0::2], AB[1::2]), key=lambda x: x[1])
current = 0
for a, b in AB_sorted:
    current += a
    if current > b:
        print("No")
        return
print("Yes")

