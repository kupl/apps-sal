n = int(input())
ans = 0
for a in range(1, n + 1):
    num = n // a
    ans += num * (num + 1) // 2 * a
print(ans)
