(n, a, b) = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    t = 0
    v = i
    while v > 0:
        t += v % 10
        v //= 10
    if a <= t <= b:
        ans += i
print(ans)
