n, m = map(int, input().split())
step = [True] * n
r = [0, 1]
MOD = 10**9 + 7
for _ in range(m):
    broken = int(input())
    step[broken - 1] = False
for i, tf in enumerate(step):
    if tf:
        r += [(r[i] + r[i + 1]) % MOD]
    else:
        r += [0]
print(r[-1])
