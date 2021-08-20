n = int(input())
ans = 0
for i in range(n):
    (a, b, c, d) = map(int, input().split())
    ans += (c - a + 1) * (d - b + 1)
print(ans)
