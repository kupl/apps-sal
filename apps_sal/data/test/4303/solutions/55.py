(n, k) = list(map(int, input().split()))
x = list(map(int, input().split()))
ans = 10 ** 9
for l in range(n - k + 1):
    r = l + k - 1
    ans = min(ans, abs(x[r]) + abs(x[r] - x[l]), abs(x[l]) + abs(x[r] - x[l]))
print(ans)
