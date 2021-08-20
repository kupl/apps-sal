n = int(input())
tab = [10 ** 8 for i in range(n + 1)]
tab[0] = 0
for i in range(n):
    now = 1
    while i + now <= n:
        tab[i + now] = min(tab[i + now], tab[i] + 1)
        now *= 6
    now = 9
    while i + now <= n:
        tab[i + now] = min(tab[i + now], tab[i] + 1)
        now *= 9
print(tab[-1])
