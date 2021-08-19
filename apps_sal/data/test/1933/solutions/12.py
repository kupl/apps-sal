(n, m, k) = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
l = list(map(list, list(zip(*l))))
(score, chx) = (0, 0)
for row in l:
    sumx = sum(row[:k])
    (val, idx) = (sumx, 0)
    for (i, j) in enumerate(row[k:]):
        sumx += j - row[i]
        if sumx > val:
            val = sumx
            idx = i
    score += val
    chx += sum(row[:idx])
print(score, chx)
