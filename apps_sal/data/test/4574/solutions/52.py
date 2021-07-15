n = int(input())
a = list(map(int, input().split()))
rods = []
tmp = {}
for i in a:
    if i in tmp:
        tmp[i] += 1
        if tmp[i] >= 2:
            rods.append(i)
            tmp[i] = 0
    else:
        tmp[i] = 1

rods.sort(reverse=True)
if len(rods) >= 2:
    print(rods[0] * rods[1])
else:
    print(0)
