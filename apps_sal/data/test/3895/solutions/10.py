a = int(input())
b = list(map(int,input().split()))
count = 1
s = set()
d = list()
f = dict()
suc = list()
succ = True
for i in b:
    if i in f:
        d.append(f[i])
    else:
        f[i] = count
        suc.append(i)
        d.append(count)
        count+=1
for i in range(len(suc)):
    if d[suc[i]-1] != i+1:
        print(-1)
        return
print(count-1)
print(*d)
print(*suc)
