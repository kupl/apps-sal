n = int(input())
c = list(map(int, input().split()))
s = [''] * n
INF = int(1e15)
not_rev = [INF] * n
rev = [INF] * n
for i in range(n):
    s[i] = input()
not_rev[0] = 0
rev[0] = c[0]
for i in range(1, n):
    if s[i - 1] <= s[i]:
        not_rev[i] = min(not_rev[i], not_rev[i - 1])
    if s[i - 1][::-1] <= s[i]:
        not_rev[i] = min(not_rev[i], rev[i - 1])
    if s[i - 1] <= s[i][::-1]:
        rev[i] = min(rev[i], not_rev[i - 1])
    if s[i - 1][::-1] <= s[i][::-1]:
        rev[i] = min(rev[i], rev[i - 1])
    rev[i] += c[i]
print(-1 if min(rev[n - 1], not_rev[n - 1]) == INF else min(rev[n - 1], not_rev[n - 1]))
