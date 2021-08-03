n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    pre = a[i]
    post = a[i + 1]
    many = pre + post - x
    if many > 0:
        ans += many
        if many <= post:
            a[i + 1] -= many
        else:
            a[i] -= many - post
            a[i + 1] = 0

print(ans)
