N = int(input())
ans = N * 2 - 2
for n in range(1, int(N**.5) + 1):
    if N % n == 0:
        ans = min(ans, N // n + n - 2)

print(ans)
