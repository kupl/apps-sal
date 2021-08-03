def read(): return list(map(int, input().split()))


n, k = read()
a = list(read())
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i - 1]
ans = 0
for i in range(1, n + 1):
    for j in range(i + k - 1, n + 1):
        t = (s[j] - s[i - 1]) / (j - i + 1)
        ans = max(ans, t)
print(ans)
