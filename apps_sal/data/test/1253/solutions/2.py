(n, k) = list(map(int, input().split()))
L = list(map(int, input().split()))
for x in range(n):
    if L[x] < 0:
        L[x] *= -1
        k -= 1
    if k == 0:
        break
if k != 0:
    L0 = list(map(abs, L))
    z = min(L0)
    j = L0.index(z)
    for _ in range(k):
        L[j] *= -1
print(sum(L))
