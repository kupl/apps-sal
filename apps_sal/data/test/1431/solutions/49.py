#!/usr/bin/env python3
n = int(input())
*a, = list(map(int, input().split()))
b = [0] * (n // 2) + a[n // 2:]
for i in reversed(list(range(n // 2))):
    b[i] = sum(b[(i + 1) * (j + 1) - 1] for j in range(n // (i + 1))) & 1 ^ a[i]
print((sum(b)))
print((*[i + 1 for i in range(n) if b[i] == 1]))
