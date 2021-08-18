N = int(input())

capa = [int(input()) for _ in range(5)]
for i in range(5):
    if capa[i] == min(capa):
        transmin = i


if capa[transmin] >= N:
    print((5))
else:
    if N % capa[transmin] == 0:
        print((transmin + N // capa[transmin] + 4 - transmin))
    else:
        print((transmin + N // capa[transmin] + 1 + 4 - transmin))
