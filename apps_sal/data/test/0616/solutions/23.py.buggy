N, M = map(int, input().split())
a = []
b = []
c = []

MY_INF = 1000000007

for _ in range(M):
    a_tmp, b_tmp = map(int, input().split())
    a.append(a_tmp)
    b.append(b_tmp)
    c.append(list(map(int, input().split())))

c_bin = []
for i in range(M):
    c_bin.append(sum([1 << (cij - 1) for cij in c[i]]))

memo = [None] * (1 << N)


def dp(state):
    nonlocal MY_INF
    if state == (1 << N) - 1:
        return 0
    if memo[state] != None:
        return memo[state]
    #
    rets = [MY_INF]
    for i in range(M):
        if (state | c_bin[i]) > state:
            rets.append(a[i] + dp((state | c_bin[i])))
    ret = min(rets)
    #
    memo[state] = ret
    return ret


ans = dp(0)
if ans != MY_INF:
    print(ans)
else:
    print(-1)
