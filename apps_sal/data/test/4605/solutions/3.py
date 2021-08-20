(n, a, b) = list(map(int, input().split()))
ans = 0
for num in range(1, n + 1):
    p = num
    digit_sum = 0
    while p > 0:
        digit_sum += p % 10
        p //= 10
    if a <= digit_sum <= b:
        ans += num
print(ans)
