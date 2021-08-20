"""
- minでの桁数
- その後の余りでgreedy
- 
"""
num_dic = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
(N, M) = list(map(int, input().split()))
t_dic = {}
A = list(map(int, input().split()))
A = sorted(A)[::-1]
for a in A:
    t_dic[a] = num_dic[a]
min_v = min(t_dic.values())
dp = [0] * (N + 8)
for i in range(N):
    for a in A:
        num = t_dic[a]
        if i != 0 and dp[i] == 0:
            continue
        dp[i + num] = max(10 * dp[i] + a, dp[i + num])
print(dp[N])
