n = int(input())
m = 1
ans = 0
for i in range(1, n + 1):
    m *= 2
    ans += m
print(ans)
