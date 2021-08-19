N = int(input())
vt = va = 1
for _ in range(N):
    (T, A) = map(int, input().split())
    kt = -(-vt // T)
    ka = -(-va // A)
    k = max(kt, ka)
    vt = k * T
    va = k * A
print(vt + va)
