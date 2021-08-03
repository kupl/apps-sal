a, b = map(int, input().split())
ans = 0
for i in range(a, b + 1):
    num = 0
    j = i
    while j > 0:
        r = j % 10
        j //= 10
        num = num * 10 + r
    if i == num:
        ans += 1


print(ans)
