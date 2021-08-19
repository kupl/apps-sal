# 12653415
# わからんが、とてもきれいですね

N, M, Q = list(map(int, input().split()))

conditions = [list(map(int, input().split())) for _ in range(Q)]


def dfs(A, max_a):
    if len(A) == N:
        num = 0
        for a, b, c, d in conditions:
            if A[b - 1] - A[a - 1] == c:
                num += d
        return num
    ans = 0
    for i in range(max_a, M + 1):
        ans = max(ans, dfs(A + [i], i))
    return ans


print(dfs([1], 1))
