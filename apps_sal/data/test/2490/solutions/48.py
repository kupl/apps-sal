n=list(map(int,input()))
keta=len(n)
satsu=0

for i in range(keta):
    tmp = n.pop()
    if i == keta-1:
        n.append(0)
    
    if tmp == 10:
        tmp=0
        n[-1]=n[-1]+1
    if tmp > 5 or (tmp==5 and n[-1] >= 5):
        satsu += 10 - tmp
        n[-1] = n[-1] + 1
    else:
        satsu += tmp

print((satsu+n[0]))

