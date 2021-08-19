(n, q) = map(int, input().strip().split())
count = [0 for i in range(n + 1)]
tot = 0
painters = []
for i in range(q):
    (l, r) = map(int, input().strip().split())
    painters.append([l, r])
    for j in range(l, r + 1):
        if count[j] == 0:
            tot += 1
        count[j] += 1
ones = [0 for i in range(n + 1)]
twos = [0 for i in range(n + 1)]
painters.sort()
for i in range(1, n + 1):
    ones[i] = ones[i - 1]
    twos[i] = twos[i - 1]
    if count[i] == 1:
        ones[i] += 1
    elif count[i] == 2:
        twos[i] += 1
mx = 0
for i in range(q):
    for j in range(i + 1, q):
        a = ones[painters[i][1]] - ones[painters[i][0] - 1]
        b = ones[painters[j][1]] - ones[painters[j][0] - 1]
        if painters[j][0] <= painters[i][1]:
            c = twos[min(painters[i][1], painters[j][1])] - twos[painters[j][0] - 1]
        else:
            c = 0
        mx = max(mx, tot - a - b - c)
print(mx)
