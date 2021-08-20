(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = [0] * m
p = []
for i in range(n + m):
    if t[i] == 1:
        p.append(i)
ans[0] = p[0]
for i in range(m):
    if i == m - 1:
        ans[i] += n + m - p[i] - 1
    else:
        for j in range(p[i] + 1, p[i + 1]):
            if a[j] - a[p[i]] <= a[p[i + 1]] - a[j]:
                ans[i] += 1
            else:
                ans[i + 1] += 1
print(' '.join(map(str, ans)))
