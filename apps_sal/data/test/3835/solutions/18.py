from math import sqrt

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
kek = []
for i in range(n):
    lol = [0, 1] if i > 1 else [1, 2] if i == 0 else [0, 2]
    a, b = lol
    kek.append(int(sqrt(arr[i][a] * arr[i][b] // arr[a][b])))
print(' '.join(map(str, kek)))

