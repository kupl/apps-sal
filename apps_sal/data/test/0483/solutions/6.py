n = int(input())
s = input().rstrip()
a = list(map(int, input().split()))
(l, r) = ([], [])
for i in range(n):
    if s[i] == 'R':
        r.append(a[i])
    else:
        l.append(a[i])
i = j = 0
ans = 10 ** 10
while i < len(r) and j < len(l):
    if r[i] < l[j]:
        ans = min(ans, l[j] - r[i])
        i += 1
    else:
        j += 1
if ans == 10 ** 10:
    print(-1)
else:
    print(ans // 2)
