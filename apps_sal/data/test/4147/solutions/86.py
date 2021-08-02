import itertools

n, a, b, c = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))
mp = float("inf")
for i in itertools.product([0, 1, 2, 3], repeat=n):
    if 0 not in i or 1 not in i or 2 not in i:
        continue
    la, lb, lc = 0, 0, 0
    temp = 0
    for j in range(3):
        temp += (i.count(j) - 1) * 10
    for j in range(n):
        if i[j] == 0:
            la += l[j]
        elif i[j] == 1:
            lb += l[j]
        elif i[j] == 2:
            lc += l[j]
    for j, k in [[la, a], [lb, b], [lc, c]]:
        temp += abs(j - k)
    mp = min(mp, temp)
print(mp)
