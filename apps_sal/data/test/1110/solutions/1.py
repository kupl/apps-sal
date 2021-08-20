n = int(input())
ans = 0
for i in range(n):
    ans += n - i
    ans += i * (n - i - 1)
print(ans)
