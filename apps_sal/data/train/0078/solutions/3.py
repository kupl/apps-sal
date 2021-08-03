q = int(input())
for query in range(q):
    n, m = list(map(int, input().split()))
    matrix = [input() for i in range(n)]
    row = [0] * n
    col = [0] * m
    for i in range(n):
        suma = 0
        for j in range(m):
            if matrix[i][j] == '*':
                suma += 1
        row[i] = suma
    for j in range(m):
        suma = 0
        for i in range(n):
            if matrix[i][j] == '*':
                suma += 1
        col[j] = suma
    wynik = 100000000000
    for i in range(n):
        for j in range(m):
            pom = m + n - 1 - (row[i] + col[j] - (1 if matrix[i][j] == '*' else 0))
            wynik = min(wynik, pom)
    print(wynik)
