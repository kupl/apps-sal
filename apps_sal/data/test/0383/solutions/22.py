#!/usr/bin/env python3

def F(n, k):
    if k < 2:
        return k
    b = [0] * (k - 1) + [1]
    for i in range(n):
        b.append(sum(b[-k:]) % (10 ** 9 + 7))
    return b[-1]


n, k, d = list(map(int, input().split()))

ans = F(n, k) - F(n, d - 1)
if ans < 0:
    ans += 10 ** 9 + 7

print(ans)
