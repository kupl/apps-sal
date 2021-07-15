x=[None]*10
y=[None]*10
t=[]
xc=[]
yc=[]
f=False
for i in range(8):
    x[i],y[i]=list(map(int,input().split()))
    if (x[i],y[i])in t: f=True
    t.append((x[i],y[i]))
    if not(x[i]  in xc): xc.append(x[i])
    if y[i] not in yc:yc.append(y[i])
            


if (len(xc)!=3)or(len(yc)!=3)or f: print('ugly')
else:
             yc.sort()
             xc.sort()
             if (xc[1],yc[1])in t:print('ugly')
             else: print('respectable')

