mod = 10**9 + 7


def A001792(n):
    if n > 1:
        return (n + 1) * pow(2, n - 2, mod)
    else:
        return 1


nn = int(input())
C = list(map(int, input().split()))
C.sort(reverse=True)
mod = 10**9 + 7
ans = 0
for i in range(nn):
    ans += pow(2, nn - i - 1, mod) * A001792(i + 1) * C[i]
    ans %= mod
ans = ans * pow(2, nn, mod)
ans %= mod
print(ans)
