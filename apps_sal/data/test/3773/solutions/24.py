def grundy(a, k):
    while a >= k:
        q = a // k
        if (a - q * k) % (q + 1) == 0: return a // k
        a -= (q + 1) * ((a - q * k) // (q + 1) + 1)
    return 0


n, = map(int, input().split())
g = 0
for _ in range(n):
    g ^= grundy(*map(int, input().split()))
print("Takahashi" if g else "Aoki")
