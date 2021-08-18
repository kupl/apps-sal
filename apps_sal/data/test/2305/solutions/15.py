def main():
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline

    N = int(input())
    C = [c - 1 for c in map(int, input().split())]
    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    size_subtree = [1] * N
    num_v = [0] * N
    ans = [0] * N

    def dfs(v_now, v_parent, color_parent):
        color_now = C[v_now]
        num_v_now = num_v[color_now]
        num_v_parent = num_v[color_parent]
        for v2 in tree[v_now]:
            if v2 == v_parent:
                continue
            dfs(v2, v_now, color_now)
            size_subtree[v_now] += size_subtree[v2]
        num_v[color_now] = num_v_now + size_subtree[v_now]
        if color_parent != -1:
            k = size_subtree[v_now] - (num_v[color_parent] - num_v_parent)
            ans[color_parent] += k * (k + 1) // 2

    dfs(0, -1, -1)

    for color in range(N):
        if color == C[0]:
            continue
        k = N - num_v[color]
        ans[color] += k * (k + 1) // 2

    numAll = N * (N + 1) // 2
    ans = [numAll - ans for ans in ans]

    print(*ans, sep='\n')


main()
