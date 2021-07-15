N, M = map(int, input().split())
Nlist, Mlist = [], []
res = []

for i in range(N):
    ab = list(map(int, input().split()))
    Nlist.append(ab)

for i in range(M):
    cd = list(map(int, input().split()))
    Mlist.append(cd)

for i in range(N):
    res = 0
    mini = float('inf')
    for j in range(M):
        calc = abs(Nlist[i][0] - Mlist[j][0]) + abs(Nlist[i][1] - Mlist[j][1])
        if calc < mini:
            mini = calc
            res = j+1
    print(res) 
