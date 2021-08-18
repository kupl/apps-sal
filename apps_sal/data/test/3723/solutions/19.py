import math

N = int(input())

S = [int(s) for s in input().split()]

factors = {}

for s in S:
    root_s = math.sqrt(s)

    for i in range(2, math.ceil(root_s) + 1, 1):
        if s % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1

            while s % i == 0:
                s //= i

    if s > 1 and s in factors:
        factors[s] += 1
    elif s > 1 and s not in factors:
        factors[s] = 1


if len(factors.values()) == 0:
    ans = 1
else:
    ans = max(factors.values())

print(ans)
