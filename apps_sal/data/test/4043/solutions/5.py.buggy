n, d, k = map(int, input().split())
num = d + 2


def solve():
    nonlocal num
    if n == 1:
        return 'NO'
    if n == 2:
        if d != 1:
            return 'NO'
        else:
            return "YES\n1 2"
    if k < 2:
        return 'NO'
    if d > n - 1:
        return 'NO'

    depth = [min(i, d - i) for i in range(d + 1)]
    ans = [(i + 1, i + 2) for i in range(d)]

    def dfs(v, depth):
        nonlocal num
        if depth == 0:
            return
        for i in range(k - 1):
            if len(ans) == n - 1:
                return
            v2 = num
            num += 1
            ans.append((v, v2))
            dfs(v2, depth - 1)

    for v in range(d + 1):
        if depth[v] == 0:
            continue
        for i in range(k - 2):
            if len(ans) == n - 1:
                break
            v2 = num
            num += 1
            ans.append((v + 1, v2))
            if depth[v] > 1:
                dfs(v2, depth[v] - 1)

    if len(ans) < n - 1:
        return "NO"
    return "YES\n%s" % "\n".join(["%d %d" % i for i in ans])


print(solve())
