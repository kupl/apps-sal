(n, x, y) = list(map(int, input().split()))
b = [0] * n
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        dist1 = j - i
        dist2 = abs(x - i) + abs(y - j) + 1
        dist3 = abs(y - i) + abs(x - j) + 1
        d = min(dist1, dist2, dist3)
        b[d] += 1
for i in range(1, n):
    print(b[i])
