n = int(input())
a = sorted(list(map(int, input().split())))
ans = sum(a)
for i in range(n):
    ans += a[i] * (i + 1)
print(ans - a[n - 1])
