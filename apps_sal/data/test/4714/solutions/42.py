a, b = list(map(int, input().split()))

ans = 0
for x in range(a, b + 1):
    if x // 10000 == x % 10 and (x // 1000) % 10 == (x // 10) % 10:
        ans += 1
print(ans)

