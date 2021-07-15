n = int(input())
d, x = list(map(int, input().split()))
arr = []
ans = 0
ans += x

for _ in range(n):
    day_sum = 1
    keisu = 1
    num = int(input())

    while day_sum <= d:
        ans += 1
        keisu += 1
        day_sum += num
print(ans)

