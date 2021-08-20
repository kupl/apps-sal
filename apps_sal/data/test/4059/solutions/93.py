n = int(input())
ans = 0
for i in range(1, 10 ** 6):
    ans += (n - 1) // i
print(ans)
