a = int(input())
bad = []
for i in range(a):
    x, y = list(map(int, input().split(' ')))
    bad.append([x, y, 0])

for i in range(a):
    for j in range(a):
        if i != j:
            if bad[j][1] == bad[i][0]:
                bad[i][2] = 1

ct = 0
for i in bad:
    if i[2] == 1:
        ct += 1

print(a - ct)
