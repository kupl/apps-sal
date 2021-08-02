n = int(input())
a = list(map(int, input().split()))

ans = 0
h = 0
for x in a:
    ans += max(0, h - x)
    h = max(h, x)

print(ans)
