from collections import defaultdict
(N, M) = list(map(int, input().split()))
L = []
A = []
for _ in range(M):
    (p, y) = list(map(int, input().split()))
    L.append([p, y])
    A.append([p, y])
L.sort(key=lambda x: x[1])
ans_d = defaultdict()
dp = [0] * (N + 1)
for (i, v) in enumerate(L):
    s = ''
    if dp[v[0]] != 0:
        l_dp = 6 - len(str(dp[v[0]] + 1))
        for j in range(l_dp):
            s += '0'
        s += str(dp[v[0]] + 1)
        dp[v[0]] += 1
    else:
        l_dp = 6 - len(str(dp[v[0]] + 1))
        for j in range(l_dp):
            s += '0'
        s += str(dp[v[0]] + 1)
        dp[v[0]] += 1
    k = str(v[0]) + ' ' + str(v[1])
    ans_d[k] = s
for i in A:
    m = str(i[0]) + ' ' + str(i[1])
    k = 6 - len(str(i[0]))
    s = ''
    for j in range(k):
        s += '0'
    s += str(i[0])
    print(s + ans_d[m])
