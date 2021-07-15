i = input()
alp= ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
res=''
r=0
for j in range(len(i))  :
    if r>0:
        r-=1
        res+=i[j]
        continue
    if j!=0 and j!=len(i)-1:
        if (i[j].upper() in alp and i[j-1].upper() in alp and i[j+1].upper() in alp) and not (i[j-1]==i[j] and i[j]==i[j+1]):
            res+=(i[j]+' ')
            r=1
            continue
        else:
            res+=i[j]
    else: res+=i[j]
print(res)
