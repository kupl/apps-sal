n = int(input())
ans = 0
cnt = 2 * n - 2
ans += (n - 3) * 4 * 3 * 3 * 4 ** (cnt - n - 2)
ans += 4 * 3 * 4 ** (cnt - n - 1) * 2
print(int(ans))
