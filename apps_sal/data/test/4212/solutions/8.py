n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]
ans = 0


def calc(A):
    score = 0
    for a, b, c, d in abcd:
        if A[b - 1] - A[a - 1] == c:
            score += d
    return score


def dfs(A, i):
    nonlocal ans
    if len(A) == n:
        ans = max(ans, calc(A))
        return
    for j in range(i, m + 1):
        A.append(j)
        dfs(A, j)
        A.pop()


dfs([], 1)
print(ans)
