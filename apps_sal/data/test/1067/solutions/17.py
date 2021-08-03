n = int(input())
a = list(map(int, input().split()))

ans = 0
zero = 0
nega = 0
for i in range(n):
    if a[i] == 0:
        zero += 1
    elif a[i] < 0:
        nega += 1
        ans += - 1 - a[i]
    else:
        ans += a[i] - 1

if nega % 2 == 1:
    if zero > 0:
        zero -= 1
        ans += 1
    else:
        ans += 2

ans += zero
print(ans)
