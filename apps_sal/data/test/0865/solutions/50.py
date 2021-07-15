def solve():
    from sys import stdin
    f_i = stdin
    
    N, T = map(int, f_i.readline().split())
    AB = [tuple(map(int, f_i.readline().split())) for i in range(N)]
    AB.sort()
    
    dp = [[0] * T for i in range(N + 1)]
    
    for i, AB_i in enumerate(AB, start=1):
        A_i, B_i = AB_i
        dp_i = dp[i]
        dp_pre = dp[i-1]
        dp_i[:A_i] = dp_pre[:A_i]
        for j, t in enumerate(zip(dp_pre[A_i:], dp_pre), start=A_i):
            x, y = t
            if x < y + B_i:
                dp_i[j] = y + B_i
            else:
                dp_i[j] = x
    
    ans = max(dp[k][-1] + AB[k][1] for k in range(N))
    print(ans)

solve()
