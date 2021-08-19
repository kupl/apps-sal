N = int(input())
mod = 10 ** 9 + 7
memo = [{} for _ in range(N + 1)]


def ok(x, y, z, nx):
    if y == 'A' and z == 'G' and (nx == 'C'):
        return False
    if x == 'A' and z == 'G' and (nx == 'C'):
        return False
    if y == 'G' and z == 'A' and (nx == 'C'):
        return False
    if y == 'A' and z == 'C' and (nx == 'G'):
        return False
    if x == 'A' and y == 'G' and (nx == 'C'):
        return False
    return True


def dfs(idx, lis):
    if idx == N:
        return 1
    (x, y, z) = (lis[0], lis[1], lis[2])
    if (x, y, z) in memo[idx]:
        return memo[idx][x, y, z]
    ret = 0
    for nx in ['A', 'G', 'C', 'T']:
        if ok(x, y, z, nx):
            ret += dfs(idx + 1, (y, z, nx))
    memo[idx][x, y, z] = ret % mod
    return ret % mod


print(dfs(0, 'DDD'))
