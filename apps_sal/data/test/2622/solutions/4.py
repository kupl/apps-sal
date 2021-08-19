(n, m) = list(map(int, input().split()))
s = []
h = []
mod = 10 ** 9
mod += 7
for i in range(n):
    s = input()
    s = s.lower()
    hw = 0
    for i in range(m):
        hw += ord(s[i]) * 10 ** (m - i)
    h.append(hw % mod)
h1 = [[] for i in range(n - m + 1)]
for i in range(m):
    hw = 0
    s = input()
    s = s.lower()
    aux = []
    for i in range(m):
        hw += ord(s[i]) * 10 ** (m - i)
    hw %= mod
    h1[0].append(hw)
    yy = 1
    for i in range(m, n):
        hw -= ord(s[i - m]) * 10 ** m
        hw *= 10
        hw += ord(s[i]) * 10
        hw %= mod
        h1[yy].append(hw)
        yy += 1
t = False
y = 0
for i in range(len(h1)):
    x = 0
    while x < n - m + 1:
        if h1[i][0] == h[x]:
            y = 0
            ans = [x + 1, i + 1]
            while y < m and h1[i][y] == h[x]:
                x += 1
                y += 1
        else:
            x += 1
        if y == m:
            break
    if y == m:
        break
print(ans[0], ans[1])
