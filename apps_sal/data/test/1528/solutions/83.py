n, x = list(map(int, input().split()))
b = 1
p = 1
for i in range(n):
    b = 2 * b + 3
    p = 2 * p + 1
x -= 1
b -= 1
ans = 0
while True:
    if x == 0:
        if b == 0:
            ans += 1
        break
    elif x == b:
        ans += p
        break
    elif x == b // 2:
        ans += p // 2 + 1
        break
    elif 0 < x < b // 2:
        x -= 1
    else:
        x -= b // 2 + 1
        ans += p // 2 + 1
    b = (b - 3) // 2
    p = (p - 1) // 2
print(ans)
