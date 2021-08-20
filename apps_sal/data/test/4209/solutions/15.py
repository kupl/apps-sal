n = int(input())
a = [int(i) for i in input().split()]
pref = [0]
d = {}
for x in range(len(a)):
    pref.append(pref[x] + a[x])
for r in range(n):
    for l in range(0, r + 1):
        v = pref[r + 1] - pref[l]
        if v in d:
            d[v].append([l, r])
        else:
            d[v] = [[l, r]]
maxi = -2
max_set = []
for key in d:
    start = -1
    tmp_set = []
    ctr = 0
    for e in range(len(d[key])):
        if d[key][e][0] > start:
            tmp_set.append(d[key][e])
            start = d[key][e][1]
            ctr += 1
    if ctr > maxi:
        maxi = ctr
        max_set = tmp_set
print(maxi)
for w in range(maxi):
    print(max_set[w][0] + 1, max_set[w][1] + 1)
