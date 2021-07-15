n = int(input())
kol = [0, 0, 0, 0, 0, 0]
ind = [4, 8, 15, 16, 23, 42]
delete = 0
for i in map(int,input().split()):
    for j in range(6):
        if ind[j] == i:
            cur = j
            break
    if cur == 0:
        kol[0] += 1
    else:
        if kol[cur-1] != 0:
            kol[cur-1] -= 1
            kol[cur] += 1
        else:
            delete += 1
print(delete + kol[0] + kol[1]*2 + kol[2]*3 + kol[3]*4 + kol[4]*5)
