def solve(n, p):
    D = {x: i for i, x in enumerate(p)}
    S = set()
    ans = []
    for x in range(1, n+1):
        for j in range(D[x]-1, x-2, -1):
            a, b = p[j], p[j+1]
            p[j+1], p[j] = p[j], p[j+1]
            D[a], D[b] = D[b], D[a]
            ans.append(j+1)
            if j in S:
                return -1
            S.add(j)
    if len(ans) != n-1:
        return -1
    return "\n".join(map(str, ans))

n = int(input())
p = list(map(int, input().split()))
print(solve(n, p))
