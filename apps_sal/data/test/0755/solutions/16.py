n = int(input())
ans = 0
for i in range(5, 0, -1):
    ans += (n // i)
    n -= (n // i * i)
print(ans)
