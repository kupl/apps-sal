n, x, m = list(map(int, input().split()))
visited = [None] * m
visited[x] = 1
a = x
s = [0] * min(n + 1, m + 1)
s[1] = x
for i in range(2, n + 1):
    a = a**2 % m
    if visited[a]:
        d = s[i - 1] - s[visited[a] - 1]
        k = i - visited[a]
        r = (n - visited[a]) % k + visited[a]
        l = (n - visited[a]) // k
        print((s[r] + l * d))
        return
    visited[a] = i
    s[i] = s[i - 1] + a
print((s[n]))
