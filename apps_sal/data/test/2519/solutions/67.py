N, K = map(int, input().split())
p = list(map(int, input().split()))

# 「和の期待値」は「期待値の和」なので、期待値を求めておく
for i in range(N):
    p[i] = (1 + p[i]) / 2

# すると結局[(p_1+1)/2,...,(p_N+1)/2]の配列から、隣接するK個の和の最大値を求めればよい
# N=10^5なので、O(N)で解く
# 2重ループは間に合わない・・・累積和！
# 累積和によって、配列上の区間の総和を求める処理を高速化！
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + p[i]
'''
S[0] = 0
S[1] = p[0]
S[2] = p[0] + p[1]
S[N] = p[0] + ... + p[N-1]

S[K]-S[0] = p[K-1] + ... + p[0]
S[K+1]-S[1] = p[K] + ... + p[1]
S[K+2]-S[2] = p[K+1] + ... + p[2]
S[N]-S[N-K] = p[N-1] + ... + p[N-K]
'''

ans = 0
# max(S[K]-S[0],S[K+1]-S[1],...,S[N]-S[N-K]) を求める
for i in range(N - K + 1):
    ans = max(ans, S[i + K] - S[i])

print(ans)
