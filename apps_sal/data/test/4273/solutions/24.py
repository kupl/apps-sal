import collections
N = int(input())
lsname = []
for i in range(N):
    name = input()
    lsname.append(name[:1])
counterN = collections.Counter(lsname)
lskey = ['M', 'A', 'R', 'C', 'H']
lsnum = []
for i in lskey:
    if i in counterN.keys():
        lsnum.append(counterN[i])
ans = 0
lenN = len(lsnum)
for i in range(lenN - 2):
    for j in range(i + 1, lenN - 1):
        for k in range(j + 1, lenN):
            ans += lsnum[i] * lsnum[j] * lsnum[k]
print(ans)
