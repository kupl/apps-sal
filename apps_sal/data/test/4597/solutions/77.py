ans = 1
N = int(input())
for i in range(1, N + 1):
    ans *= i
    ans %= 10 ** 9 + 7
print(ans)
