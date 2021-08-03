n = int(input())
ans = 0
for i in range(n):
    a, b = (int(x) for x in input().split())
    c = b - a + 1
    ans += c

print(ans)
