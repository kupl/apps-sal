def solve():
    N, M = map(int, input().split())
    S = map(int, input().split())
    *T, = map(int, input().split())
    dp = [1]*(M+1)
    for s in S:
        is_s = s.__eq__
        dp_ = dp[:]
        acc = 0
        for i, t in enumerate(T):
            if is_s(t):
                acc += dp_[i]
            dp[i+1] = dp_[i+1] + acc
    res = (dp[-1])%(10**9+7)
    return str(res)
 
def __starting_point():
    print(solve())
__starting_point()
