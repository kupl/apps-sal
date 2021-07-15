def solve():
    p, f = map(int, input().split())
    cnts, cntw = map(int, input().split())
    s, w = map(int, input().split())
    if s > w:
        s, w = w, s
        cnts, cntw = cntw, cnts
    ans = 0
    for i in range(cnts + 1):
        if s * i > p:
            break
        j = min((p - s * i) // w, cntw)
        u = min(cnts - i, f // s)
        v = min(cntw - j, (f - s * u)  // w)
        ans = max(ans, i + j + u + v)
    print(ans)
t = int(input())
for _ in range(t):
    solve()
