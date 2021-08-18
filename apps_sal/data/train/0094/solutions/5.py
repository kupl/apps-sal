input = __import__('sys').stdin.readline
for _ in range(int(input())):
    n, T = map(int, input().split())
    s = list(map(int, input().split()))
    ans = [0] * n
    g = {}
    for i in range(n):
        if T - s[i] in g:
            ans[i] = 1 - ans[g[T - s[i]]]
        g[s[i]] = i
    print(*ans)
