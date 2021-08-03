n, k = (int(i) for i in input().split())
ans = 0
d = n
for i in range(min(k, n // 2)):
    ans += (d * 2 - 3)
    d -= 2
print(ans)
