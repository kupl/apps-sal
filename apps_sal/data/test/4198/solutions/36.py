(a, b, x) = list(map(int, input().split()))
ans = 0
for i in range(11):
    nokori = max(0, x - b * i)
    ans = max(ans, min(10 ** i - 1, nokori // a))
print(min(10 ** 9, ans))
