(N, M) = map(int, input().split())
edge_out = [[] for i in range(N)]
edge_in = [[] for i in range(N + 1)]
for i in range(M):
    (s, t) = map(int, input().split())
    edge_out[s].append(t)
    edge_in[t].append(s)
edge_sum = [len(edge_out[i]) for i in range(N)]
dp = [0.0] * (N + 1)
dp[N - 1] = 1.0
for i in range(N - 2, 0, -1):
    dp[i] = 1 + sum((dp[j] for j in edge_out[i])) / edge_sum[i]
p_to_i = [0] * (N + 1)
p_to_i[1] = 1
for i in range(2, N + 1):
    p_to_i[i] = sum((p_to_i[j] / edge_sum[j] for j in edge_in[i]))
t = 0
for i in range(1, N - 1):
    if edge_sum[i] == 1:
        continue
    t = max(t, p_to_i[i] * (dp[i] - 1 - ((dp[i] - 1) * edge_sum[i] - max((dp[j] for j in edge_out[i]))) / (edge_sum[i] - 1)))
print(dp[1] - t)
