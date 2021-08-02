n, x = (int(x) for x in input().split())


ans = 0
for i in range(1, n + 1):
    if x % i == 0:
        j = x // i
        if 1 <= j <= n:
            ans += 1

print(ans)
