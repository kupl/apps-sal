n, ans, last = int(input()), 0, 0
a = list(map(int, input().split()))
for i in range(len(a)):
    while last > 0 and a[i] >= 2:
        ans += 1
        a[i] -= 2
        last -= 1
    ans += a[i] // 3
    last += a[i] % 3
print(ans)
