a, b, c = list(map(int, input().split()))

mod = 998244353

ta = a * (a + 1) // 2
tb = b * (b + 1) // 2
tc = c * (c + 1) // 2

ans = (ta * tb) % mod
ans = (ans * tc) % mod

print(ans)
