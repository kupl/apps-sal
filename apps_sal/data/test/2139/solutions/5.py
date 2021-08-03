s = input().strip()
n = len(s)
x = []
for i in range(n - 3):
    if s[i:i + 4] == 'bear':
        x.append(i)
i = 0
j = 0
ans = 0
m = len(x)
while i < m:
    ans += max(0, n - x[i] - 3)
    j += 1
    if j > x[i]:
        i += 1
print(ans)
