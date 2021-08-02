from math import gcd
from collections import defaultdict

N, P = map(int, input().split())
S = list(map(int, input()))

answer = 0
if P == 2 or P == 5:
    for j in range(N - 1, -1, -1):  # enumerate right endpoint
        if S[j] % P == 0:
            answer += j + 1
else:
    cnts = defaultdict(int)
    suffix = 0
    base = 1
    for i in range(N - 1, -1, -1):
        suffix = (suffix + S[i] * base) % P
        answer += cnts[suffix]  # Substr with length >= 2
        answer += 1 if suffix == 0 else 0  # Substr with length = 1
        cnts[suffix] += 1
        base = base * 10 % P

print(answer)
