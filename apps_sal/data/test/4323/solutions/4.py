n, m = list(map(int, input().split()))
s = []
k = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    m -= a
    s.append(a - b)
s.sort(reverse=True)
while (m < 0) and (k < n):
    m += s[k]
    k += 1
if m < 0:
    print(-1)
else:
    print(k)
