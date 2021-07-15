def dfs(inp, stat, u):
    if stat[u] > 1:
        return stat[u] < 3
    stat[u] = 2
    for v in inp[u]:
        if dfs(inp, stat, v):
            return True
    stat[u] = 3
    return False


def main():
    ans = []
    n, m = list(map(int, input().split()))
    inp = tuple(([] for _ in range(n + 1)))
    for _ in range(m):
        u, v = list(map(int, input().split()))
        ans.append((u > v) + 1)
        inp[u].append(v)
    stat = [1] * (n + 1)
    for u in range(n + 1):
        if dfs(inp, stat, u):
            print(2)
            print(*ans)
            break
    else:
        print(1)
        print(*(1,) * m)


main()

