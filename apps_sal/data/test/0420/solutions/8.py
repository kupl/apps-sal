def symetry(a, n, m):
    symmetry = 0
    k = n // 2
    for x in range(n):
        for y in range(m):
            k = n - x - 1
            if k < n - 1 and a[x][y] != a[k][y]:
                symmetry = 1
    return symmetry


(n, m) = list(map(int, input().split()))
list_anmi = [list(map(int, input().split())) for i in range(n)]
sym = 0
while n % 2 == 0:
    if symetry(list_anmi[0:n], n, m) == 0:
        n = n // 2
    else:
        break
sym = n
print(sym)
