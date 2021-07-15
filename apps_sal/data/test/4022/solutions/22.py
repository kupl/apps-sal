from collections import Counter

z=int(input())
x1_pos=[]
x2_pos=[]
ch=0
while ch<z:
    x,xx=list(map(int,input().split()))
    x1_pos.append(x)
    x2_pos.append(xx)
    ch+=1
n1=max(x1_pos)
n2=min(x2_pos)
if n1<=n2:
    first=n2-n1
    c1=Counter(x1_pos)
    c2=Counter(x2_pos)
    if c1[n1] ==1:
        index_max=x1_pos.index(n1)
        savex1=x1_pos[index_max]
        savex2=x2_pos[index_max]
        x1_pos[index_max]=min(x1_pos)
        x2_pos[index_max]=max(x2_pos)
        different=min(x2_pos)-max(x1_pos)
        x1_pos[index_max]=savex1
        x2_pos[index_max]=savex2
        if different>first:
            first=different
    if c2[n2] == 1:
        index_min=x2_pos.index(n2)
        savex2=x2_pos[index_min]
        savex1=x1_pos[index_min]
        x2_pos[index_min]=max(x2_pos)
        x1_pos[index_min]=min(x1_pos)
        different=min(x2_pos)-max(x1_pos)
        x2_pos[index_min]=savex2
        x1_pos[index_min]=savex1
        if different>first:
            first=different
    print(first)
else:
    first=0
    c1 = Counter(x1_pos)
    c2 = Counter(x2_pos)
    if c1[n1] == 1:
        index_max = x1_pos.index(n1)
        savex1 = x1_pos[index_max]
        savex2 = x2_pos[index_max]
        x1_pos[index_max] = min(x1_pos)
        x2_pos[index_max] = max(x2_pos)
        different = min(x2_pos) - max(x1_pos)
        x1_pos[index_max] = savex1
        x2_pos[index_max] = savex2
        if different > first:
            first = different
    if c2[n2] == 1:
        index_min = x2_pos.index(n2)
        savex2 = x2_pos[index_min]
        savex1 = x1_pos[index_min]
        x2_pos[index_min] = max(x2_pos)
        x1_pos[index_min] = min(x1_pos)
        different = min(x2_pos) - max(x1_pos)
        x2_pos[index_min] = savex2
        x1_pos[index_min] = savex1
        if different > first:
            first = different
    print(first)

