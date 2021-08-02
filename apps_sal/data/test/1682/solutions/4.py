n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [[b[i] - a[i], i] for i in range(n)]
c.sort()
c = c[::-1]
ans = 0
for i in range(k):
    ans += a[c[i][1]]
i = k
while i < n and c[i][0] > 0:
    ans += a[c[i][1]]
    i += 1
while i < n:
    ans += b[c[i][1]]
    i += 1
print(ans)
