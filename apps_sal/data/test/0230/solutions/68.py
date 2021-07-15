import random
from collections import defaultdict


def atoi(s):
    return ord(s) - ord("a") + 1


N = int(input())
S = input()

mod = (1 << 61) - 1
b = random.randint(10000, mod - 1)


l = 0
r = (N + 1) // 2 + 1
while r - l > 1:
    d = (r + l) // 2
    memo = defaultdict(int)
    isok = False
    h = 0
    t = pow(b, d, mod)
    for i in range(d):
        h = (h * b + atoi(S[i])) % mod
    memo[h] = 1
    for i in range(1, N - d + 1):
        h = (h*b + atoi(S[i+d-1]) - t * atoi(S[i-1])) % mod
        if not memo[h]:
            memo[h] = i + 1
        elif memo[h] and i - memo[h] + 1 >= d:
            isok = True
    if isok:
        l = d
    else:
        r = d

print(l)
