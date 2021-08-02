def main():
    from sys import stdin, stdout
    from array import array
    n, m = list(map(int, stdin.readline().split()))
    n += 1
    g = [array('l', ()) for _ in range(n)]
    for _ in range(m):
        u, v = list(map(int, stdin.readline().split()))
        g[u].append(v)
        g[v].append(u)
    ans = 0
    new = array('i', (1,)) * n
    vr = 0
    for v1 in range(n):
        if new[v1]:
            if v1 < vr:
                ans += 1  # v1 vr
            stack = [v1]
            while stack:
                u = stack.pop()
                if new[u]:
                    new[u] = 0
                    vr = max(vr, u)
                    for v in g[u]:
                        stack.append(v)
    print(ans)


main()
