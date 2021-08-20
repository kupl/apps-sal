n = int(input())
a = list(map(int, input().split()))
ans = 0
power = 0
prev = 0
for i in range(n):
    if power + prev - a[i] < 0:
        dif = -(power + prev - a[i])
        prev += dif
        ans += dif
    power += prev - a[i]
    prev = a[i]
print(ans)
