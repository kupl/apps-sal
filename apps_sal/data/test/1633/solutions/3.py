def has_rect(mat, step):
    mat[step[0]][step[1]] = True
    steps = ((0, 0), (0, 1), (1, 0), (1, 1))
    coefs = ((1, 1), (-1, 1), (1, -1), (-1, -1))
    for c in coefs:
        for s in steps:
            x = step[0] + c[0] * s[0]
            y = step[1] + c[1] * s[1]
            if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y]:
                continue
            else:
                break
        else:
            return True
    return False


(n, m, k) = map(int, input().split())
mat = [[0 for x in range(m)] for x in range(n)]
for i in range(k):
    step = tuple(map(int, input().split()))
    step = (step[0] - 1, step[1] - 1)
    if has_rect(mat, step):
        print(i + 1)
        break
else:
    print(0)
