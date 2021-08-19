(n, m) = map(int, input().split())
s = n + m
x = list(map(int, input().split()))
loc = input().split()
t = []
for i in range(s):
    if loc[i] == '1':
        t.append(i)
for i in range(m):
    ans = 0
    if i != 0:
        for j in range(t[i - 1] + 1, t[i]):
            if x[j] - x[t[i - 1]] > x[t[i]] - x[j]:
                ans += 1
    else:
        ans += t[i]
    if i != m - 1:
        for j in range(t[i] + 1, t[i + 1]):
            if x[j] - x[t[i]] <= x[t[i + 1]] - x[j]:
                ans += 1
    else:
        ans += s - t[i] - 1
    print(ans, end=' ')
