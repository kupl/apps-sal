# D - Match Matching

N, M = map(int, input().split())
A = list(int(x) for x in input().split())
match_list = [('0', 6), ('1', 2), ('2', 5), ('3', 5), ('4', 4), ('5', 5), ('6', 6), ('7', 3), ('8', 7), ('9', 6)]
MA = []
for a in A:
    MA.append(match_list[a])
MA.sort(key=lambda x: x[0], reverse=True)

# dp[i] := i本のマッチを使って作れる最大桁数
dp = [-1] * (N + 1)
dp[0] = 0
for i in range(N + 1):
    for j in range(M):
        if i - MA[j][1] >= 0:
            dp[i] = max(dp[i], dp[i - MA[j][1]] + 1)

remain_keta = dp[N]
remain_match = N
ans = ''
for i in range(dp[N]):
    for ma in MA:
        # 大きい数字から一桁使った時に、
        # 残り桁がちょうど一桁減っている場合
        if remain_match >= ma[1] and dp[remain_match - ma[1]] == remain_keta - 1:
            ans += ma[0]
            remain_keta -= 1
            remain_match -= ma[1]
            break

print(ans)
