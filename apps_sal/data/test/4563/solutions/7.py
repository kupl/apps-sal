N = int(input())
(TNow, ANow) = (int(T) for T in input().split())
for TN in range(1, N):
    (TNext, ANext) = (int(T) for T in input().split())
    Magn = max(TNow // TNext + (TNow % TNext != 0), ANow // ANext + (ANow % ANext != 0))
    (TNow, ANow) = (TNext * Magn, ANext * Magn)
print(TNow + ANow)
