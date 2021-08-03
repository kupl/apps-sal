import sys
fin = sys.stdin

n, m = map(int, fin.readline().split())

noRoad = [tuple(map(int, fin.readline().split())) for i in range(m)]
canBeCenter = [True] * n
for i, j in noRoad:
    canBeCenter[i - 1] = canBeCenter[j - 1] = False

for i in range(n):
    if canBeCenter[i]:
        print(n - 1)
        for j in range(n):
            if i != j:
                print(i + 1, j + 1)
        break
else:
    print('Я неправильно решил задачу')
