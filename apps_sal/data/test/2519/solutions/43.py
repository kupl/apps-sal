
N, K = map(int, input().split())
P = list(map(int, input().split()))


E = [0]
tot = 0
for p in P:
    tot += (p + 1) / 2
    E.append(tot)


m = 0
for i in range(N - (K - 1)):
    _ = E[i + K] - E[i]
    if _ > m:
        m = _

print(m)
