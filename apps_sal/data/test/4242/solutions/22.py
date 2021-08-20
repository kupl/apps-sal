(a, b, k) = map(int, input().split())
L = []
n = a
if a < b:
    n = b
for i in range(n):
    if a % (i + 1) == 0 and b % (i + 1) == 0:
        L.append(i + 1)
L = sorted(L, reverse=True)
print(L[k - 1])
