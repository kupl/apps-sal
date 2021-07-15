N = int(input())
ans = 10 ** N - 2 * 9 ** N + 8 ** N
ans %= (10 ** 9 + 7)
print(ans)
