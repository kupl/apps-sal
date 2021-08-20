n = int(input())
a = [[0] * n for _ in range(n)]


def od(i, j):
    k = min(i + 1, n - i)
    return abs(j - n // 2) < k


(u, v) = (0, 0)
for i in range(n):
    for j in range(n):
        if od(i, j):
            u += 1
            a[i][j] = u * 2 - 1
        else:
            v += 1
            a[i][j] = v * 2
print('\n'.join([' '.join(map(str, x)) for x in a]))
