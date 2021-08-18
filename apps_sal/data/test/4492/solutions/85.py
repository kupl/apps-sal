n, x = map(int, input().split())
a = list(map(int, input().split()))

t = 0
ans = 0
for i in a:
    s = max(0, t + i - x)
    t = i - s
    ans += s
print(ans)
