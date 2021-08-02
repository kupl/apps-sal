def cv(r, n, d):
    s = [0] * (2 * n + 1)
    q = n
    ans = 0
    s[q] = 1
    z = 0
    for i in range(n):
        if d[i] < r:
            q -= 1
            z -= s[q]
        else:
            z += s[q]
            q += 1
        ans += z
        s[q] += 1
    return ans


n, r = map(int, input().split())
d = list(map(int, input().split()))
print(cv(r, n, d) - cv(r + 1, n, d))
