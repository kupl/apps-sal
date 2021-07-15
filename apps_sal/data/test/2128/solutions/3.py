#!/usr/bin/env python3
import sys
input = sys.stdin.readline
MOD = 998244353
 
n = int(input())
a = [int(item) for item in input().split()]
A = 0
B = 0
child = 1
bases = []
base = 1
for i in range(n + 10):
    bases.append(base)
    base *= 100
    base %= MOD

for i, item in enumerate(a):
    A += child * (100 - item) * bases[n-i-1]
    A %= MOD
    B += child * (100 - item) * bases[n-i-1] * (i + 1)
    B %= MOD
    child *= item
    child %= MOD
B += child * n
ans = B * pow(bases[n]-A, MOD-2, MOD)
ans %= MOD
print(ans)
