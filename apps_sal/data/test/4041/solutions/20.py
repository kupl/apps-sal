s = input()
t = input()
n = len(s)
m = len(t)
le = []
ri = []
ans = 0
p = 0
for i in range(n):
    if p < m:
        if s[i] == t[p]:
            le.append(i)
            if p == m - 1:
                ans = max(ans, n - 1 - i)
            p += 1
p = m - 1
for j in range(n - 1, -1, -1):
    if p >= 0:
        if s[j] == t[p]:
            ri.append(j)
            if p == 0:
                ans = max(ans, j - 0)
            p -= 1
ri.reverse()
for k in range(m - 1):
    ans = max(ans, ri[k + 1] - le[k] - 1)
print(ans)
