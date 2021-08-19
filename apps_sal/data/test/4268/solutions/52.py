(n, d) = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(i + 1, n):
        sumpos = 0
        for k in range(d):
            sumpos += (pos[i][k] - pos[j][k]) ** 2
        for l in range(sumpos + 1):
            if l ** 2 == sumpos:
                count += 1
print(count)
