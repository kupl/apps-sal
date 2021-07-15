from collections import defaultdict
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))

d = defaultdict(int)
dh = defaultdict(list)
dhs = []
s = 0
for i in range(n):
    for j in range(i+1,n):
        try:
            t = (a[j][1]-a[i][1])/(a[j][0]-a[i][0])
            if d[t]==0:
                d[t] = 1
                dh[t].append(i)
                dh[t].append(j)
            else:
                if i not in dh[t] and j not in dh[t]:
                    d[t]+=1
                dh[t].append(i)
                dh[t].append(j)
        except:
            if s==0:
                s+=1
            elif i not in dhs and j not in dhs:
                s+=1
            dhs.append(i)
            dhs.append(j)

t = list(d.keys())
c = 0
l = 0
for i in t:
    k = d[i]
    l+=k
    c+=((k)*(k-1))//2

c+=((s)*(s-1))//2
l += s
l = (l*(l-1))//2
print(l-c)

