x = []
tt = int(input())
for i in range(tt):
    (a, b, c, d) = list(map(int, input().split(' ')))
    x.append([a, b, c, d])
ct = 0
for a in range(1, 101):
    for b in range(1, 101):
        for i in x:
            (a1, a2, a3, a4) = (i[0], i[1], i[2], i[3])
            if a1 <= a <= a3 and a2 <= b <= a4:
                ct += 1
print(ct)
