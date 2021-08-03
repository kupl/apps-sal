N, W = map(int, input().split())
w_v = [list(map(int, input().split())) for i in range(N)]

memo = {}


def nap(i, j):
    if i == N:
        return 0

    if (i, j) in memo:
        return memo[i, j]
    elif w_v[i][0] > j:
        temp = nap(i + 1, j)
    else:
        temp = max(nap(i + 1, j), nap(i + 1, j - w_v[i][0]) + w_v[i][1])
    memo[i, j] = temp

    return memo[i, j]


print(nap(0, W))
