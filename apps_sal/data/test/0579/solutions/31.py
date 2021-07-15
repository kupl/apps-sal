from numba import njit
from sys import maxsize


@njit
def solve(n, k, p, c):
    used = [0] * n
    ss = []
    for i in range(n):
        if used[i]:
            continue
        now = i
        s = []
        while not used[now]:
            used[now] = 1
            s.append(c[now])
            now = p[now]
        ss.append(s)

    res = -maxsize
    for s in ss:
        s_len = len(s)
        cumsum = [0]
        # 2周分の累積和
        for i in range(2*s_len):
            cumsum.append(cumsum[-1] + s[i%s_len])

        max_sum = [-maxsize] * s_len
        for i in range(s_len):
            for j in range(s_len):
                max_sum[j] = max(max_sum[j], cumsum[i+j] - cumsum[i])

        for i in range(s_len):
            if i > k:
                continue
            v = (k - i) // s_len
            if i == 0 and v == 0:
                continue
            if cumsum[s_len] > 0:
                res = max(res, max_sum[i] + cumsum[s_len] * v)
            elif i > 0:
                res = max(res, max_sum[i])
    print(res)


def __starting_point():
    n, k = list(map(int, input().split()))
    p = list([int(x)-1 for x in input().split()])
    c = list(map(int, input().split()))
    solve(n, k, p, c)

__starting_point()
