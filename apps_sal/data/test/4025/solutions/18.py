f = [0, 1, 2, 0, 2, 1, 0]
l = [int(i) for i in input().split()]
mn = min([l[i] // f.count(i) for i in range(3)])
l = [l[i] - mn * f.count(i) for i in range(3)]

mx = 0
for i in range(7):
    tmp = l.copy()
    j = 0
    while tmp[f[(i + j) % 7]] > 0:
        tmp[f[(i + j) % 7]] -= 1
        j += 1
    if j > mx:
        mx = j
print(mn * 7 + mx)

