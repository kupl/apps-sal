n = int(input())
A = list(map(int,input().split()))

ans = 0
for bit in range(60):
    m = 1 << bit
    c = sum(a & m for a in A) >> bit
    ans += (c * (n - c)) << bit
    ans %= (10**9+7)
print(ans)
