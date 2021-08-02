n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

s = sum(a[:k])
ans = s / (n - k + 1)
for i in range(n - k):
    s = s + a[i + k] - a[i]
    ans += s / (n - k + 1)
print(ans)
