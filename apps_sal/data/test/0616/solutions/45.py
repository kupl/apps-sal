MOD = 10 ** 9 + 7
INF = 10 ** 11
import sys
sys.setrecursionlimit(100000000)

def main():
    N,M = list(map(int,input().split()))
    key = []
    for _ in range(M):
        a,b = list(map(int,input().split()))
        c = list(map(int,input().split()))
        can_open = 0
        for i in c:
            can_open ^= 1<<(i - 1)
        key.append((a,can_open))
    
    dp = [[INF] * (1<<N) for _ in range(M + 1)]
    for i in range(M):
        dp[i][0] = 0
    
    for i in range(M):
        price,can_open = key[i]
        for s in range(1,1<<N):
            dp[i + 1][s] = min(dp[i][s],dp[i][(s&can_open)^s] + price)
    print((dp[-1][-1] if dp[-1][-1] != INF else -1))

def __starting_point():
    main()

__starting_point()
