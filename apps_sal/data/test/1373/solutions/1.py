N, K = map(int, input().split())
mod = 10**9 + 7

Ans = 0

for m in range(K,N+2): # m個選ぶ m = K ~ N+1
    # 1刻みで全ての数を作ることができる
    # よって答えは、作れる数の　(最大値) - (最小値) 通りとなる

    # 最大値 = 大きい方からm個選ぶ = N-m+1 ~ N までの和
    maxi = m*(N-m+1 + N)/2

    # 最小値 = 小さい方からm個選ぶ = 0~m-1を選ぶ
    mini = m*(0 + m-1)/2

    Ans += int(maxi - mini + 1)
    Ans %= mod
    
print(Ans)
