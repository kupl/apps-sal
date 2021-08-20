n = int(input())
a = list(map(int, input().split()))
ans = 2 * 10 ** 14 + 1
s = sum(a)
x = 0
y = s
for i in range(n - 1):
    x += a[i]
    y -= a[i]
    ans = min(ans, abs(x - y))
print(ans)
