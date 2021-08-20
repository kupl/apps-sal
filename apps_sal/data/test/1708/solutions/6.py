def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


(n, m) = mi()
a = li()
c = li()
x = list(range(n))
x.sort(key=lambda i: (c[i], i))
cur = 0
out = []
for i in range(m):
    (t, d) = mi()
    p = min(d, a[t - 1])
    d -= p
    a[t - 1] -= p
    ans = c[t - 1] * p
    while d:
        while cur < n and a[x[cur]] == 0:
            cur += 1
        if cur == n:
            ans = 0
            break
        p = min(d, a[x[cur]])
        d -= p
        a[x[cur]] -= p
        ans += c[x[cur]] * p
    out.append(str(ans))
print(*out, sep='\n')
