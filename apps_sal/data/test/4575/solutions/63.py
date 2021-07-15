n = int(input())
d, x = map(int, input().split())
al = list(int(input()) for _ in range(n))

ans = x

for a in al:
    day = 1
    while day <= d:
        ans += 1
        day += a

print(ans)
