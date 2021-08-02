q = int(input())
for i in range(q):
    a = int(input())
    cycle = [1 for i in range(a)]

    tab = list(map(int, input().split()))

    for indice, j in enumerate(tab):
        var = indice + 1

        while tab[var - 1] != indice + 1:
            var = tab[var - 1]
            cycle[indice] += 1

    print(*cycle)
