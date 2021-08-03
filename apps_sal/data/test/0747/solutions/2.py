def solve(p, n, x, t, h, m):
    used, xx, ans = [0] * n, x, 0
    while (True):
        k = -1
        for i in range(n):
            if (used[i] == 0) and (t[i] == p) and (h[i] <= xx) and ((k == -1) or (m[i] > m[k])):
                k = i
        if (k == -1):
            break
        ans += 1
        xx += m[k]
        used[k] = 1
        p = p ^ 1
    return ans


n, x = map(int, input().split())
t, h, m = [0] * n, [0] * n, [0] * n
for i in range(n):
    t[i], h[i], m[i] = map(int, input().split())
print(max(solve(0, n, x, t, h, m), solve(1, n, x, t, h, m)))
