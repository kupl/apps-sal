n = int(input())
a = list(map(int, input().split()))

s = a[0]
t = sum(a) - a[0]

i = 0
ans = abs(s - t)
for i in range(1, n - 1):
    s += a[i]
    t -= a[i]
    ans = min(ans, abs(s - t))
    i += 1
print(ans)
