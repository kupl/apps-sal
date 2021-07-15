def resolve():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    dp = [[-1 for _ in range(2)] for __ in range(45)]
    dp[0][0] = 0

    for i in range(40):
        mask = 1<<(40-i-1)
        one_num = 0
        for a in A:
            if a & mask:
                one_num += 1
        costdiff0 = mask*one_num
        costdiff1 = mask*(N-one_num)
        if dp[i][1] != -1:
            dp[i+1][1] = max(dp[i+1][1], dp[i][1]+max(costdiff0, costdiff1))
        if dp[i][0] != -1 and K&mask: 
            dp[i+1][1] = max(dp[i+1][1], dp[i][0]+costdiff0)
        if dp[i][0] != -1:
            if K&mask:
                dp[i+1][0] = max(dp[i+1][0], dp[i][0]+costdiff1)
            else:
                dp[i+1][0] = max(dp[i+1][0], dp[i][0]+costdiff0)
    print(max(dp[40][0], dp[40][1]))

    

if '__main__' == __name__:
    resolve()
