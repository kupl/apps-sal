n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    shortest = 4 * 10**8 + 5
    for j in range(m):
        distance = abs(a[i][0] - b[j][0]) + abs(a[i][1] - b[j][1])
        if distance < shortest:
            idx = j
            shortest = distance
    print(idx + 1)
