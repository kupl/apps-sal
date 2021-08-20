import sys
dist = []
for i in range(10):
    t = []
    for j in range(10):
        t.append([32] * 10)
    dist.append(t)
for i in range(10):
    for j in range(10):
        row = dist[i][j]
        for a in range(10):
            for b in range(10):
                val = (a * i + b * j) % 10
                s = a + b
                if s > 0 and s < row[val]:
                    row[val] = s
        for k in range(10):
            if row[k] == 32:
                row[k] = -1
            else:
                row[k] -= 1
d = [int(i) for i in input()]
data = [(d[i + 1] - d[i]) % 10 for i in range(len(d) - 1)]
for i in range(10):
    for j in range(10):
        ans = 0
        for d in data:
            inc = dist[i][j][d]
            if inc == -1:
                ans = -1
                break
            else:
                ans += inc
        sys.stdout.write(str(ans) + ' ')
    sys.stdout.write('\n')
