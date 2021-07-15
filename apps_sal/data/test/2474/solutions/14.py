N = int(input())
C = sorted(map(int, input().split()))
mod = 10**9+7
# そのビットが異なる確率 * それ以上のビットが立っている数の期待値 * c
ans = 0
for i, c in enumerate(C[::-1], 2):
    ans += i * c
ans %= mod
ans = ans * pow(2, 2*N-2, mod) % mod
print(ans)

