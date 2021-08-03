def II(): return int(input())
def LII(): return list(map(int, input().split()))


n = II()
town = [LII() for _ in range(n)]

distance = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        [xi, yi] = town[i]
        [xj, yj] = town[j]

        distance += ((xi - xj)**2 + (yi - yj)**2)**0.5

print(distance * 2 / n)
