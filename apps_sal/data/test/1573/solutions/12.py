(n, d) = list(map(int, input().split()))
res = []
for i in range(n):
    res.append(list(map(int, input().split())))
res.sort()
res.reverse()
res.append([0, 0])
left = 0
right = 0
summ = 0
rsumm = 0
while True:
    while res[left][0] - d < res[right][0]:
        summ += res[right][1]
        right += 1
        if right == n + 1:
            break
    if right == n + 1:
        break
    rsumm = max(summ, rsumm)
    summ -= res[left][1]
    left += 1
rsumm = max(summ, rsumm)
print(rsumm)
