#!/usr/bin/env python3
import sys
input = sys.stdin.readline
import bisect

def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

n, m, k = map(int, input().split())
a = [int(item) for item in input().split()] + [0]
b = [int(item) for item in input().split()] + [0]

acnt = []
bcnt = []
c = 0
for item in a:
    if item == 1:
        c += 1
    else:
        acnt.append(c)
        c = 0
c = 0
for item in b:
    if item == 1:
        c += 1
    else:
        bcnt.append(c)
        c = 0
acnt.sort()
bcnt.sort()

ans = 0
div = divisors(k)
for a_val in div:
    b_val = k // a_val
    a_idx = bisect.bisect_left(acnt, a_val)
    b_idx = bisect.bisect_left(bcnt, b_val)
    a_total = sum(acnt[a_idx:]) - (len(acnt) - a_idx) * (a_val - 1)
    b_total = sum(bcnt[b_idx:]) - (len(bcnt) - b_idx) * (b_val - 1)
    ans += a_total * b_total

print(ans)
