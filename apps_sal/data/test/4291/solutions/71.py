N, Q = map(int, input().split())
S = input()

l = [0] * Q
r = [0] * Q

cntac = [0]

for t in range(1, N):
    if S[t - 1:t + 1] == "AC":
        cntac.append(cntac[t - 1] + 1)
    else:
        cntac.append(cntac[t - 1])

for i in range(Q):
    l[i], r[i] = map(int, input().split())

    print(cntac[r[i] - 1] - cntac[l[i] - 1])
