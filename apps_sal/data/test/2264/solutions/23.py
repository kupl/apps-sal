test = int(input())
for _ in range(test):
    n = int(input())
    mas = 0
    minA = 10**10
    maxB = -1
    for __ in range(n):
        mas = list(map(int, input().split()))
        minA = min([minA, mas[1]])
        maxB = max([maxB, mas[0]])
    if maxB > minA:
        print(maxB - minA)
    else: print(0)
