def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    P = list(map(int, input().split()))
    X = list(map(int, input().split()))

    child = [[] for _ in range(N+1)]
    par = [-1] * (N+1)
    for i, p in enumerate(P):
        child[p].append(i+2)
        par[i+2] = p
    child_num = [len(child[i]) for i in range(N+1)]
    st = []
    for i in range(1, N+1):
        if child_num[i] == 0:
            st.append(i)
    dp = [None] * (N+1)
    ok = 1
    while st:
        v = st.pop()
        x = X[v-1]
        if v != 1:
            p = par[v]
            child_num[p] -= 1
            if child_num[p] == 0:
                st.append(p)
        if not child[v]:
            dp[v] = (x, 0)
            continue
        dp2 = [[False] * (x+1) for _ in range(len(child[v])+1)]
        dp2[0][0] = True
        S = 0
        for i, u in enumerate(child[v]):
            a, b = dp[u]
            S += a+b
            for j in range(x+1):
                if dp2[i][j]:
                    if j + a <= x:
                        dp2[i+1][j+a] = True
                    if j+b <= x:
                        dp2[i+1][j+b] = True
        finish = 1
        for j in range(x, -1, -1):
            if dp2[-1][j]:
                dp[v] = (x, S-j)
                finish = 0
                break
        if finish:
            ok = 0
            break

    if ok:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


def __starting_point():
    main()

__starting_point()
