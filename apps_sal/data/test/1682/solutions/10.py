n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * n
ans = sum(b)
for i in range(n):
    c[i] = a[i] - b[i]
c.sort()
i = 0
while (i < k) or (i < n and c[i] < 0):
    ans += c[i]
    i += 1
print(ans)
