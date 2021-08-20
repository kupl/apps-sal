def solve(h, w, A, B):
    center = (h + w) * 80
    C = [[abs(A[r][c] - B[r][c]) for c in range(w)] for r in range(h)]
    dp = [[0] * w for r in range(h)]
    dp[0][0] = 1 << center + C[0][0] | 1 << center - C[0][0]
    for r in range(h):
        for c in range(w):
            if r > 0:
                dp[r][c] |= dp[r - 1][c] << C[r][c] | dp[r - 1][c] >> C[r][c]
            if c > 0:
                dp[r][c] |= dp[r][c - 1] << C[r][c] | dp[r][c - 1] >> C[r][c]
    mask = bin(dp[-1][-1] >> center)
    return mask[::-1].find('1')


(h, w) = map(int, input().split())
A = [list(map(int, input().split())) for i in range(h)]
B = [list(map(int, input().split())) for i in range(h)]
print(solve(h, w, A, B))
