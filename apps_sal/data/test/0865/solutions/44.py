def solve():
    import numpy as np
    from sys import stdin
    f_i = stdin
    
    N, T = map(int, f_i.readline().split())
    AB = [tuple(map(int, f_i.readline().split())) for i in range(N)]
    AB.sort()
    max_Ai = AB[-1][0]
    
    dp = [[0] * T for i in range(N + 1)]
    dp = np.zeros(max_Ai + T, dtype=int)
    
    
    for A_i, B_i in AB:
        dp[A_i:A_i+T] = np.maximum(dp[A_i:A_i+T], dp[:T] + B_i)
    
    print(max(dp))

solve()
