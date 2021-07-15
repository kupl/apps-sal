#参考
#https://atcoder.jp/contests/abc179/submissions/16904040

MOD = 998244353
 
def solve(lr, dp, n):
    acc_dp = [1] * n    # 累積和
    for i in range(1, n):
        val = 0
        for d in lr: # 各区間について区間和を求め足していく
            a = i - d[0]
            if a < 0:
                continue
            b = i - d[1] - 1 
            val += acc_dp[a] - (acc_dp[b] if b >= 0 else 0) # 区間和を素早く求める
        dp[i] = val % MOD
        acc_dp[i] = (acc_dp[i - 1] + dp[i]) % MOD
    return dp[n - 1]
 
 
def main():
    f = open(0)
    n, k = [int(x) for x in f.readline().split()]
    lr = [[int(x) for x in f.readline().split()] for _ in range(k)]
    dp = [0] * n
    dp[0] = 1
    ans = solve(lr, dp, n)
    print(ans)
 
main()
