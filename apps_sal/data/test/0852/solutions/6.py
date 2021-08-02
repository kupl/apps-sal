T = int(input())
for _ in range(T):
    N, K, L = list(map(int, input().split()))
    D = list(map(int, input().split()))
    P = list(range(K)) + list(range(K, 0, -1))
    dp = [[0] * (len(P)) for _ in range(N + 1)]
    for i in range(len(P)):
        dp[0][i] = 1
    for i in range(N):
        for _ in range(2):
            for j in range(len(P)):
                if dp[i][j] == 0:
                    continue
                if i and dp[i][(j + 1) % len(P)] == 0 and D[i - 1] + P[(j + 1) % len(P)] <= L:
                    dp[i][(j + 1) % len(P)] = 1
                if D[i] + P[(j + 1) % len(P)] <= L:
                    dp[i + 1][(j + 1) % len(P)] = 1
    print('No' if all(a == 0 for a in dp[-1]) else 'Yes')
