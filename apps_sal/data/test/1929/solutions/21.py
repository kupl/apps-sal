(n, t, c) = list(map(int, input().split()))
a = list(map(int, input().split()))
nos = ans = 0
lst = -1
for i in range(0, n):
    if a[i] > t:
        ans += max(i - c - lst, 0)
        lst = i
ans += max(n - lst - c, 0)
print(ans)
