k = [list(map(int, input().split())) for x in range(3)]
k[0][0] = 1
k[1][1] = sum(k[0]) - sum(k[1])
k[2][2] = sum(k[0]) - sum(k[2])
s = k[0][1] + k[0][2]
x = min(k[0][0], k[1][1], k[2][2]) - 1
if x <= 0:
    k[0][0] -= x
    k[1][1] -= x
    k[2][2] -= x
while k[1][1] + k[2][2] != s:
    k[0][0] += 1
    k[1][1] += 1
    k[2][2] += 1
for i in k:
    for j in i:
        print(j, end=' ')
    print()
