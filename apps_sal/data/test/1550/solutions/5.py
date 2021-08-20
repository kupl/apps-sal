n = int(input())
l = list(input())
for i in range(n):
    l[i] = int(l[i])
ans = 10 ** (n - 1)
for i in range(n):
    l = l[1:] + l[:1]
    m = []
    for j in range(n):
        m.append(l[j])
    for j in range(1, n):
        m[j] -= m[0]
        if m[j] < 0:
            m[j] += 10
    m[0] = 0
    cur = ''
    for j in range(n):
        cur += str(m[j])
    ans = min(ans, int(cur))
ans = str(ans)
while len(ans) < n:
    ans = '0' + ans
print(ans)
