N = int(input())
vt = va = 0
for _ in range(N):
    (T, A) = map(int, input().split())
    kt = -(-vt // T)
    ka = -(-va // A)
    k = max(kt, ka, 1)
    vt = k * T
    va = k * A
print(vt + va)
