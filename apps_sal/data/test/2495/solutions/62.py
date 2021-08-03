n = int(input())
a = list(map(int, input().split()))


ans = 0
ansans = 0
now = 0

for i in range(n):
    now += a[i]
    if i % 2 == 0:
        if now < 0:
            ans += abs(now) + 1
            now = 1
        elif now == 0:
            ans += 1
            now = 1
    else:
        if now >= 0:
            ans += abs(now) + 1
            now = -1
        elif now == 0:
            ans += 1
            now = -1

now = 0
for i in range(n):
    now += a[i]
    if i % 2 == 0:
        if now > 0:
            ansans += abs(now) + 1
            now = -1
        elif now == 0:
            ansans += 1
            now = -1
    else:
        if now < 0:
            ansans += abs(now) + 1
            now = 1
        elif now == 0:
            ansans += 1
            now = 1

print((min(ans, ansans)))
