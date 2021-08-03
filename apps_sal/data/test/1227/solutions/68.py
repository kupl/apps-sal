N = list(map(int, input()))
K = int(input())


dp = [[[0] * 2 for _ in range(K + 1)] for _ in range(len(N) + 1)]
dp[0][0][0] = 1
for i in range(len(N)):
    for j in range(K + 1):
        for is_smaller in range(2):
            for l in range(10):
                if not is_smaller and l > N[i] or l != 0 and j + 1 > K:
                    continue
                i_ = i + 1
                j_ = j
                is_smaller_ = is_smaller

                if l != 0:
                    j_ += 1

                if not is_smaller and l < N[i]:
                    is_smaller_ = 1
                dp[i_][j_][is_smaller_] += dp[i][j][is_smaller]
print((dp[len(N)][K][0] + dp[len(N)][K][1]))
