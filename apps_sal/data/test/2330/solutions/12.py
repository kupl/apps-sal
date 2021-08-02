t = int(input())
for i in range(t):
    n, m = list(map(int, input().split()))
    dop = list(map(int, input().split()))
    suma = sum(dop)
    mas = []
    for i in range(n):
        mas.append([dop[i], i])
    if m < n or n == 2:
        print(-1)
        continue
    mas.sort()
    print(suma * 2 + (mas[0][0] + mas[1][0]) * (m - n))
    for i in range(1, n):
        print(i, i + 1)
    print(n, 1)
    for i in range(m - n):
        print(mas[0][1] + 1, mas[1][1] + 1)
