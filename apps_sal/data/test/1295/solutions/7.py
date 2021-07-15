t = input
p = print
r = range
n, m = map(int, t().split())
a = list(map(int, t().split()))
b = list(map(int, t().split()))
ans = 0
i = 0
for j in a:
    while i < m - 1 and abs(j - b[i]) >= abs(j - b[i + 1]):
        i += 1
    ans = max(ans, abs(j - b[i]))
p(ans)
