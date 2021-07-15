
def resolve():
    S = input()
    K = int(input())
    N = len(S)

    # dp[i][j][smaller]
    # i桁目まで見たときに0以外の数字をｊ個使用し、条件を満たす個数
    # smaller:
    # 0:i桁目まで見たときに一致している(次の桁は余裕が無い)
    # 1:次の桁は余裕がある

    dp = [[[0]*2 for _ in range(4)] for _ in range(N+1)]
    dp[0][0][0] = 1

    for i in range(N):
        for j in range(4):
            for smaller in range(2):
                now = int(S[i])
                for d in range(10):
                    ni = i+1
                    nj = j
                    n_smaller = smaller
                    if d != 0:
                        nj += 1
                    if nj > K:
                        continue
                    if smaller == 0:
                        if d > now: # 値を超えている
                            continue
                        if d < now: # 次の桁は余裕がある
                            n_smaller = 1
                    dp[ni][nj][n_smaller] += dp[i][j][smaller]
    ans = dp[N][K][0] + dp[N][K][1]
    print(ans)


def __starting_point():
    resolve()

__starting_point()
