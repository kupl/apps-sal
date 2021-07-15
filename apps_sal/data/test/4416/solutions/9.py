#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
both = []
alice = []
bob = []
for _ in range(n):
    c, a, b = map(int, input().split())
    if a and b:
        both.append(c)
    elif a:
        alice.append(c)
    elif b:
        bob.append(c)

alice.sort()
bob.sort()
for a, b in zip(alice, bob):
    both.append(a + b)
both.sort()

if len(both) < k:
    print(-1)
else:
    print(sum(both[:k]))
