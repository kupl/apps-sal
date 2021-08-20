(n, k) = [int(i) for i in input().split()]
ans = 0
for i in range(min(n // 2, k)):
    ans += (n - i * 2 - 2) * 2
    ans += 1
print(ans)
