i = list([int(c) for c in input()])

d = sum([i[3] - i[0], i[4] - i[1], i[5] - i[2]])

if(d < 0):
    i.reverse()
    d *= -1

for z in range(3):
    i[z] = 9 - i[z]

i = sorted(i)
i.reverse()

ir = 0
for (ind, z) in enumerate(i):
    if ir >= d:
        print(ind)
        break
    ir += z
