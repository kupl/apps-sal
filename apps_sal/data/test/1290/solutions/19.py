(n, m) = (int(i) for i in input().split())
tab = [0] * n
for i in [int(j) for j in input().split()]:
    tab[i - 1] += 1
print(min(tab))
