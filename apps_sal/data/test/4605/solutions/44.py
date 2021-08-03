n, a, b = list(map(int, input().split()))
ans = 0

for i in range(1, n + 1):
    sum = 0
    x = i
    while x > 0:
        sum += x % 10
        x //= 10
    if a <= sum and sum <= b:
        ans += i

print(ans)
