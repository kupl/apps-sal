import sys
sys.setrecursionlimit(10 ** 7)


def solve(G, p, ans, st, fst, arr, x):
    arr[p] = x
    cnt_1 = 0
    z = -1
    for nxt in G[p]:
        if nxt in st:
            cnt_1 += 1
            z = nxt
    cnt_2 = 0
    for v in st:
        if p in G[v]:
            cnt_2 += 1
    if cnt_1 > 1 or cnt_2 > 1:
        return False
    elif cnt_1 == 1 and cnt_2 == 1:
        if fst in G[p]:
            for v in st:
                ans.append(v)
            return True
        else:
            k = arr[z]
            for v in st:
                if arr[v] >= k:
                    ans.append(v)
            return True
    for nxt in G[p]:
        st.add(nxt)
        if solve(G, nxt, ans, st, fst, arr, x + 1):
            return True
        st.remove(nxt)
    arr[p] = 0
    return False


def main():
    n, m = map(int, input().split())
    G = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        G[a].append(b)
    ans = []
    f = False
    st = set()
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        st.add(i)
        if solve(G, i, ans, st, i, arr, 1):
            f = True
            break
        st.remove(i)
    if f:
        print(len(ans))
        ans.sort()
        for v in ans:
            print(v)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
