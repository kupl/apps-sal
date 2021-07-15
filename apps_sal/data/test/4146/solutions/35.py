n = int(input())
al = list(map(int, input().split()))

ol =al[::2]
el =al[1::2]

from collections import Counter
col = Counter(ol)
cel = Counter(el)
scol = sorted(col.items(), key=lambda x: x[1], reverse=True)  
scel = sorted(cel.items(), key=lambda x: x[1], reverse=True)  
scol.append(("x",0))
scel.append(("y",0))


temp = scol[0][1] + scel[0][1]

if scol[0][0]==scel[0][0]:
    temp2 = scol[0][1]+scel[1][1]
    temp3 = scol[1][1]+scel[0][1]
    print(n-max(temp2,temp3))
    
else:
    print(n-temp)
