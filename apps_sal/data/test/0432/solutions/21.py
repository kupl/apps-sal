import collections


def do():
    n = int(input())
    costs = [int(c) for c in input().split(' ')]
    next = [int(c) - 1 for c in input().split(' ')]
    ind = [0] * n
    for (i, c) in enumerate(next):
        if i != c:
            ind[c] += 1
    seen = [0] * n
    res_seen = [0] * n
    res = 0

    def get(entry):
        m = costs[entry]
        p = entry
        while True:
            if res_seen[p]:
                return 0
            res_seen[p] = 1
            m = min(m, costs[p])
            p = next[p]
            if p == entry:
                break
        return m

    def dfs(i):
        stack = [i]
        seen[i] = 1
        while stack:
            cur = stack.pop()
            nei = next[cur]
            if seen[nei]:
                return get(nei)
            seen[nei] = 1
            stack.append(nei)
        return 0
    for i in range(n):
        if ind[i] == 0:
            res += dfs(i)
    for i in range(n):
        if seen[i] == 0:
            res += dfs(i)
    return res


print(do())
