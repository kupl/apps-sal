def main():
    N, M = map(int, input().split())
    A = set(map(int, input().split()))


    cost = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    B = []
    for i in range(1, 10):
        if i in A:
            B.append((cost[i], i))

    B = B[::-1]
    dp = [[-1, -1] for i in range(N+1)]
    dp[0][0] = 0
    for i in range(1, N+1):
        for x, y in B:
            if i >= x and dp[i-x][0] >= 0:
                if dp[i][0] < dp[i-x][0] + 1:
                    dp[i][0] = dp[i-x][0] + 1
                    dp[i][1] = y
    id = N
    ans = []
    # print(dp)
    while(id > 0):
        ans.append(dp[id][1])
        id -= cost[dp[id][1]]
    ans.sort(reverse=True)
    print("".join(map(str, ans)))
main()
