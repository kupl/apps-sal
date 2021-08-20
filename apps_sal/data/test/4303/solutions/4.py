(n, k) = map(int, input().split())
x = list(map(int, input().split()))
ans = 10 ** 18
for i in range(n - k + 1):
    temp = 0
    temp += min(abs(x[i]), abs(x[i + k - 1])) + abs(x[i] - x[i + k - 1])
    ans = min(ans, temp)
print(ans)
