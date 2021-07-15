import math

N = int(input())

S = [int(s) for s in input().split()]
max_s = max(S)

factors = [set() for i in range(max_s + 1)]
fact_cnt = [0] * (max_s + 1)

for p in range(2, max_s + 1):
    if factors[p] != set():
        continue
    else:
        for i in range(p, max_s + 1, p):
            factors[i].add(p)

# print(factors)

for s in S:
    for p in factors[s]:
        fact_cnt[p] += 1

ans = max(1, max(fact_cnt))

print(ans)
