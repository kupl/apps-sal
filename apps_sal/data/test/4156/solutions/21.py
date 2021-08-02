n, w = list(map(int, input().split()))
L = list(map(int, input().split()))
maxim = 0
minin = 0
summa = 0
for i in range(n):
    summa += L[i]
    if summa > maxim:
        maxim = summa
    if summa < minin:
        minin = summa
print(max(0, w - maxim + minin + 1))
