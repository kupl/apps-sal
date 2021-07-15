N = int(input())
n = len(str(N))
ans = 0
for i in range(1, n+1):
    if i == n and n % 2 != 0:
        ans += N - 10 ** (n - 1) + 1
        break
    elif i % 2 != 0:
        ans += 9 * 10 ** (i - 1)
print(ans)
