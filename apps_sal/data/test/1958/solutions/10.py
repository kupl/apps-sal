(n, p) = [int(x) for x in input().split()]
guys = [input() == 'halfplus' for i in range(n)]
cur = 0
S = 0
for guy in reversed(guys):
    S += p * cur + guy * p // 2
    cur = 2 * cur + 1 if guy else 2 * cur
print(S)
