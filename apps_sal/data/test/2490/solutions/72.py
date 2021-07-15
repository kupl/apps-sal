N = input()
X = list(map(int, list(str(N))))

dp1 = [float('inf')] * (len(X) + 1)  # dp1[i] := 上からi番目の金額を丁度払う場合の最小値
dp2 = [float('inf')] * (len(X) + 1)  # dp2[i] := 上からi番目の金額を１周り大きい額で支払う場合の最小値
dp1[0] = 0
for i, x in enumerate(X):
    dp1[i + 1] = min(dp1[i] + x, dp2[i] + x)
    dp2[i + 1] = min(dp1[i] + (10 - x) + 1, dp2[i] + (10 - x) - 1)

print((min(dp1[-1], dp2[-1])))

