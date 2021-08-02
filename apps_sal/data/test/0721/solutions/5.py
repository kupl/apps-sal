#!/usr/local/bin/python3

n, d = list(map(int, input().split()))
a = list(map(int, input().split()))
m = int(input())

a.sort()

if m <= n:
    result = sum(a[:m])
else:
    result = sum(a) - (m - n) * d

print(result)
