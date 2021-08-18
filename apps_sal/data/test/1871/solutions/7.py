
n, x = list(map(int, input().split()))

cs = sorted(map(int, input().split()))


summa = 0
for c in cs:
    summa += x * c
    x = (x - 1 if x - 1 >= 1 else 1)

print(summa)
