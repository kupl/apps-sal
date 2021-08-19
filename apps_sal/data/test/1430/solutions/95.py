(n, k) = list(map(int, input().split()))
s = list(input())
cnt = []
if s[0] == '0':
    cnt.append(0)
i = 0
while i < n:
    j = i
    while j < n and s[j] == s[i]:
        j += 1
    cnt.append(j - i)
    i = j
if s[-1] == '0':
    cnt.append(0)
m = len(cnt)
cs = [0] * (m + 1)
for i in range(m):
    cs[i + 1] = cs[i] + cnt[i]
ans = 0
for l in range(0, m + 1, 2):
    r = l + 2 * k + 1
    if r > m:
        r = m
    ans = max(ans, cs[r] - cs[l])
print(ans)
