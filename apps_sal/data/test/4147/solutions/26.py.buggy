def dfs(ka, kb, kc, cnta, cntb, cntc, phase):
    nonlocal ans
    if phase == n:
        if 0 < cnta and 0 < cntb and 0 < cntc:
            ans = min(ans, abs(a - ka) + abs(b - kb) + abs(c - kc) + 10 * (cnta + cntb + cntc - 3))
        return
    dfs(ka + l[phase], kb, kc, cnta + 1, cntb, cntc, phase + 1)
    dfs(ka, kb + l[phase], kc, cnta, cntb + 1, cntc, phase + 1)
    dfs(ka, kb, kc + l[phase], cnta, cntb, cntc + 1, phase + 1)
    dfs(ka, kb, kc, cnta, cntb, cntc, phase + 1)


n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]
ans = 10**9
dfs(0, 0, 0, 0, 0, 0, 0)
print(ans)
