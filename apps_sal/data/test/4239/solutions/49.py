def solve():
    n = int(input())
    dp = [True] + [False]*(n+1)
    way = [1] + [6**i for i in range(1,9) if 6**i <= n] + [9**i for i in range(1,7) if 9**i <= n]
    loop_counter = 0
    while True:
        loop_counter += 1
        newdp = [False] * (n+1)
        for w in way:
            for i in range(w, n+1):
                if newdp[i]: continue
                if dp[i-w]: newdp[i] = True
                if newdp[n]: 
                    return loop_counter
        dp = [x for x in newdp]

print(solve())
