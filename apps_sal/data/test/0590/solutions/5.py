n = int(input())
l = list(map(int, input().split()))
lis, ind = set(), {}
for i in l:
    if i in ind:
        ind[i] += 1
    else:
        ind[i] = 1
        lis.add(i)
mlis = sorted(set(range(1, n + 1)) - lis, key=int)
k = 0
for i, j in enumerate(l):
    if ind[j] != 1:
        if ind[j] == 0 or mlis[k] < j:
            l[i] = mlis[k]
            k += 1
            if k == len(mlis):
                break
        else:
            ind[j] = 0
        if ind[j] > 1:
            ind[j] -= 1

print(len(mlis), " ".join(map(str, l)), sep='\n')
