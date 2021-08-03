num = int(input())
data = dict()

lst = input().split()
lst = list(map(int, lst))

for i in range(num):
    if lst[i] in data:
        data[lst[i]][0] += 1
        data[lst[i]][2] = i
    else:
        data[lst[i]] = [1, i, i]

m = 1
newlst = []
for n in data.keys():
    info = data[n]
    if info[0] > m:
        m = info[0]
        newlst = [info[1:]]
    elif info[0] == m:
        newlst += [info[1:]]

mn = num + 1
best = []
newlst = sorted(newlst)
for i in range(len(newlst)):
    rng = newlst[i][1] - newlst[i][0]
    if rng < mn:
        mn = rng
        best = newlst[i]

print(best[0] + 1, best[1] + 1)
