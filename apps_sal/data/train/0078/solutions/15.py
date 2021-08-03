for TT in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    mat = [[1 if c == '*' else 0 for c in input()] for _ in range(n)]
    h = [sum(l) for l in mat]
    v = [0] * m
    for i in range(n):
        for j in range(m):
            v[j] += mat[i][j]
    res = float('inf')
    for i in range(n):
        for j in range(m):
            val = (n - h[i]) + (m - v[j])
            if mat[i][j] == 0:
                val -= 1
            res = min(res, val)
    print(res)
