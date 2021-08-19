n = int(input())
ms1 = 0
mt1 = 20000000000
ms2 = 0
mt2 = 20000000000
for _ in range(n):
    (s, t) = [int(x) for x in input().split()]
    ms1 = max(ms1, s)
    mt1 = min(mt1, t)
m = int(input())
for _ in range(m):
    (s, t) = [int(x) for x in input().split()]
    ms2 = max(ms2, s)
    mt2 = min(mt2, t)
dif = max(ms1 - mt2, ms2 - mt1)
print(max(0, dif))
