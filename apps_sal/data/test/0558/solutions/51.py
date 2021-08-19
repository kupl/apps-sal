# 解説通り
N, M, K = list(map(int, input().split()))
m = 998244353
ans = (M * pow(M - 1, N - 1, m)) % m  # すべて違う色,k=0
alpha = 1  # n-1Ck, k=0の値で初期化
for k in range(1, K + 1):
    alpha = (alpha * (N - k) * pow(k, m - 2, m)) % m  # 逆元で計算しないとTLE
    ans = (ans + M * alpha * pow(M - 1, N - k - 1, m)) % m
print(ans)
