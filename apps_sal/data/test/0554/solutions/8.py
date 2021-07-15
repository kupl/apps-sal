n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = []
for i in range(m):
    l, r = list(map(int, input().split()))
    s = 0
    for j in range(l - 1, r):
        s += a[j]
    b.append(s)
b.sort()
i = len(b) - 1
ans = 0
while (i >= 0 and b[i] > 0):
    ans += b[i]
    i -= 1
print(ans)
