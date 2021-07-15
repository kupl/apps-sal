n, k = list(map(int, input().split()))
s = input()

a = []

i = 0
while i < n:
    j = 1
    while i + j < n and s[i] == s[i + j]:
        j += 1
    a.append((s[i], j))
    i += j
if a[0][0] == '0':
    a = [('1', 0)] + a
if a[-1][0] == '1':
    a.append(('0', 0))

while len(a) < k * 2:
    a.append(('1', 0))
    a.append(('0', 0))
m = len(a)


s = [0] * (m + k * 5 + 1)
for i in range(m + k * 2):
    if i < m:
        s[i + 1] = s[i] + a[i][1]
    else:
        s[i + 1] = s[i]
ans = 0
for i in range(1, m, 2):
    ans = max(ans, s[i + k * 2] - s[i - 1])
print(ans)

