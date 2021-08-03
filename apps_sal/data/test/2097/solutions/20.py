t = int(input())
for k in range(t):
    n = int(input())
    mas = list(map(int, input().split()))
    kol = 0
    for i in range(n):
        if mas[i] == 0:
            mas[i] = 1
            kol += 1
    print(kol + int(sum(mas) == 0))
