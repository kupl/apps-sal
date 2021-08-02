n, b, d = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
i = 0

while i < n:
    sum = 0
    while sum <= d and i < n:
        if a[i] <= b:
            sum += a[i]
        i += 1
    if sum > d:
        ans += 1

print(ans)
