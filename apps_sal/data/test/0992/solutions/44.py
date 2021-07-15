import numpy as np

def main():
    MOD = 998244353
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    # dp = [[0] * (S + 1) for i in range(N + 1)]
    # dp[0][0] = 1
    
    dp = np.zeros(S + 1, np.int64)
    dp[0] = 1
    
    for i, a in enumerate(A, start=1):
        # i - 1 番目までの数で 合計が X になる組み合わせが
        # dp[i-1][X] 個あるのであれば、
        # そのdp[i-1][X] 個 のそれぞれに対してAi を加える/加えないの
        # 2パターンが考えられるので、dp[i-1]を2倍する
        dp_next = 2 * dp
        
        # さらに、i - 1 番目までの数で 合計が X - Ai になる組み合わせが
        # dp[i-1][X - Ai] 個ある場合、
        # i番目の数(Ai)を足すことで合計をXにできる
        dp_next[a:] += dp[:-a] # dp[:-a] = dp[:len(dp)-a]       

        # 大きくなりすぎないように逐次MODをとる
        dp_next %= MOD
        
        dp = dp_next

    # print(*dp, sep='\n')
    print(dp[S])

def __starting_point():
    main()
__starting_point()
