ans, cur = 0, 1 << 179
for i in range(int(input())):
    a, p = list(map(int, input().split()))
    cur = min(cur, p)
    ans += a * cur
print(ans)

