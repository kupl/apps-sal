n = int(input())
s = input()
a = [0] * 100005
ans, maxn = 0, 0

for i in range(0, n):
    if(s[i] == 'G'):
        if i == 0:
            a[0] = 1
        else:
            a[i] = a[i - 1] + 1
        maxn = max(maxn, a[i])
        ans += 1
for i in range(n - 2, -1, -1):
    if (s[i] == 'G'):
        a[i] = max(a[i], a[i + 1])
for i in range(0, n):
    if(i > 0 and i < n - 1 and s[i] == 'S' and s[i - 1] == 'G' and s[i + 1] == 'G' and a[i - 1] + a[i + 1] != ans):
        maxn = max(maxn, a[i - 1] + a[i + 1] + 1)
        continue
    if (i > 0 and i < n - 1 and s[i] == 'S' and s[i - 1] == 'G' and s[i + 1] == 'G'):
        maxn = max(maxn, a[i - 1] + a[i + 1])
        continue
    if(s[i] == 'G' and a[i] != ans):
        maxn = max(maxn, a[i] + 1)
print(maxn)
