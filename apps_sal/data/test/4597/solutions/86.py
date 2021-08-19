n = int(input())
ans = 1
for i in range(1, n + 1):
    ans *= i
    if ans >= 10 ** 9 + 7:
        ans %= 10 ** 9 + 7
print(ans)
