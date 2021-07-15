import sys
sys.setrecursionlimit(10 ** 6)
N, K = map(int, input().split())
mod = 10 ** 9 + 7
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)


def dfs(K, u, p):
    if p == -1:
        can_use_color_num = K - 1
    else:
        can_use_color_num = K - 2

    # if K < len(edges[u]):
    #     return 0
    # else:
    case_num = 1
    for e in edges[u]:
        if e == p:
            continue
        case_num *= can_use_color_num
        can_use_color_num -= 1
        case_num %= mod
    for e in edges[u]:
        if e == p:
            continue
        case_num *= dfs(K, e, u)
        case_num %= mod
    return case_num

ans = K * dfs(K, 0, -1)
ans %= mod
print(ans)
