S = input()
N = len(S)

# 最終的な結果は '0101...' or '1010...' の2通り
# 2通りとのハミング距離の最小値を求める

a1, a2 = 0, 0
# '0101...' との距離
for i in range(N):
    if i % 2 == 0 and S[i] == '1':
        a1 += 1  # 奇数番目
    if i % 2 == 1 and S[i] == '0':
        a1 += 1  # 偶数番目
# '1010...' との距離
for i in range(N):
    if i % 2 == 0 and S[i] == '0':
        a2 += 1  # 奇数番目
    if i % 2 == 1 and S[i] == '1':
        a2 += 1  # 偶数番目
print(min(a1, a2))
