n, a = int(input()), list(map(int, input().split()))
ans = 20000
for i in range(1, n - 1):
    b = a[:i] + a[i + 1:]
    ans = min(ans, max(b[j + 1] - b[j] for j in range(n - 2)))
print(ans)
