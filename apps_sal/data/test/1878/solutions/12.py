n = int(input())
ans = 0
for i in range(n):
    a, b, c, d = map(int, input().split())
    ans += (abs(c - a) + 1)  * (abs(d - b) + 1)
print(ans)
