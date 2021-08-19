#!/usr/bin/env python3

n = int(input())
d, x = list(map(int, input().split()))
a = [int(input()) for i in range(n)]

d -= 1
ans = 0
for i in a:
    ans += d // i + 1

print((ans + x))
