(n, m) = list(map(int, input().split()))
s = input()
mod = 10 ** 9 + 7
(c, b, ans, d, k) = (0, 0, 0, [[1]], n - m)
for i in s:
    c += (i == '(') * 2 - 1
    b = min(c, b)
for i in range(n - m):
    nd = d[-1][1:] + [0] * 2
    for j in range(1, i + 2):
        nd[j] = (nd[j] + d[-1][j - 1]) % mod
    d.append(nd)
for i in range(k + 1):
    for j in range(-b, min(k - i - c, i) + 1):
        ans = (ans + d[i][j] * d[k - i][j + c]) % mod
print(ans)
