t = int(input())
for q in range(t):
    n = int(input())
    mas = list(map(int, input().split()))
    mas.sort()
    maxi = 1
    for i in range(n):
        if i + 1 >= mas[i]:
            maxi = i + 2
    print(maxi)
