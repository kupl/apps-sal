n=int(input())
m=[]
sc=[]
for i in range(n):
    m.append(input())
    sc.append(set(m[i]))
    if len(sc[i])!=len(m[i]):
        print('NO')
        break
else:
    i=0
    pX=False
    while i<len(m):
        j=i+1
        p=False
        while j<len(m):
            #print(m)
            z=len(sc[i].intersection(sc[j]))
            #a=len(sc[i])
            #b=len(sc[j])
            if m[i] in m[j]:
                m[i]=m[j]
                sc[i]=sc[j]
                sc.pop(j)
                m.pop(j)
                p=True
                break
            elif m[j] in m[i]:
                sc.pop(j)
                m.pop(j)
                j-=1
            elif z>0:
                if m[i][-z:]==m[j][:z]:
                    m[i]+=m[j][z:]
                elif m[j][-z:]==m[i][:z]:
                    m[i]=m[j]+m[i][z:]
                else:
                    pX=True
                    break
                sc[i]=set(m[i])
                m.pop(j)
                sc.pop(j)
                j-=1
                p=True
            j+=1
        if not p:
            i+=1
        if pX:
            print('NO')
            break
    if not pX:
        print(''.join(sorted(m)))
