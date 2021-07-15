q=input()
q1=input().split()
q2=input().split()
parr1=[]
for i in range(0,len(q1),2):
    pair=(q1[i],q1[i+1])
    parr1.append(pair)
parr2=[]
for i in range(0,len(q2),2):
    pair=(q2[i],q2[i+1])
    parr2.append(pair)
matches1={}
matches2={}
for i in parr1:
    for j in parr2:
        if (i[0]==j[0] and i[1]==j[1]) or (i[0]==j[1] and i[1]==j[0]):
            continue
        elif i[0]==j[0] or i[0]==j[1]:
            if matches1.get(i)==None or matches1.get(i)==i[0]:
                matches1[i]=i[0]
            else:
                print('-1')
                quit()
            if matches2.get(j)==None or matches2.get(j)==i[0]:
                matches2[j]=i[0]
            else:
                print('-1')
                quit()
        elif i[1]==j[1] or i[1]==j[0]:
            if matches1.get(i)==None or matches1.get(i)==i[1]:
                matches1[i]=i[1]
            else:
                print('-1')
                quit()
            if matches2.get(j)==None or matches2.get(j)==i[1]:
                matches2[j]=i[1]
            else:
                print('-1')
                quit()
        else:
            pass
matches=list(matches1.values())
for i in range(0,len(matches)):
    if matches[i]==matches[i-1]:
        pass
    else:
        print('0')
        quit()
print(matches[0])

