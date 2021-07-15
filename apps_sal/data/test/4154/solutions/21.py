N,M = map(int, input().split())

Lm = -1
Rm = float('inf')

for _ in range(M):
    L,R = map(int, input().split())
    Lm = max(L, Lm)
    Rm = min(R, Rm)

print(max(Rm - Lm + 1, 0))
