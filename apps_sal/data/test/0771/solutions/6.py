tmp = list(map(int,input().split()))
n,k,m = tmp[0],tmp[1],tmp[2]
a = list(map(int,input().split()))

d = {}
for i in a:
    tmp = i % m
    if tmp not in d:
        d[tmp] = [i]
    else:
        d[tmp].append(i)

OK = False
for i in range(m):
    if i in d and len(d[i]) >= k:
        OK = True
        print('Yes')
        for j in d[i][:k]:
            print(j,end=" ")
        break
if not OK:
    print("No")
