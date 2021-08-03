N, K = map(int, input().split())
p = list(map(int, input().split()))

# max_list = []
# max_sum = 0

# for i in range(N - K + 1):
# 	if sum(p[i:i + K]) >= max_sum:
# 		max_sum = sum(p[i:i+K])
# 		max_list = p[i:i + K]
# ans = 0
# for n in max_list:
# 	ans += (n + 1) / 2

# print(ans)
expected = [0] * N
for i in range(N):
    expected[i] = (p[i] + 1) / 2

ans = 0
agg = 0
for i in range(N):
    if i < K:
        agg += expected[i]
    else:
        agg += expected[i]
        agg -= expected[i - K]
    ans = max(ans, agg)
print(ans)
