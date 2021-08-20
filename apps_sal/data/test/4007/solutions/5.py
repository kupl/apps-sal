n = int(input())
l = list(map(int, input().split()))
dostal = [0] * (n + 1)
for i in range(n):
    dostal[l[i]] = 1
do_dania = []
ind = []
for i in range(n):
    if l[i] == 0:
        ind.append(i)
for i in range(1, n + 1):
    if dostal[i] == 0:
        do_dania.append(i)
j = 0
for i in range(n):
    if l[i] == 0:
        l[i] = do_dania[j]
        j += 1
for i in range(len(ind) - 1):
    if l[ind[i]] == ind[i] + 1:
        kk = l[ind[i]]
        l[ind[i]] = l[ind[i + 1]]
        l[ind[i + 1]] = kk
if l[ind[-1]] == ind[-1] + 1:
    kk = l[ind[-1]]
    l[ind[-1]] = l[ind[0]]
    l[ind[0]] = kk
print(*l)
