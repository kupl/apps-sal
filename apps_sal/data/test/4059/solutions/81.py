n = int(input())
ans = 0
for a in range(1, n):
    ans += (n - 1) // a
print(ans)
