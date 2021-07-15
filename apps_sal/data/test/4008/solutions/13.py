n,k=[int(x) for x in input().split()]
mas=[int(x) for x in input().split()]
tot=[]
dic={}
for i in range(k):
    dic[i+1]=set()
    dic[i+1].add(mas[i])
    tot.append(i+1)
for item in range(k,len(mas)):
    for i in range(k):
        if mas[item] not in dic[i+1]:
            tot.append(i+1)
            dic[i+1].add(mas[item])
            break
    else:
        print('NO')
        break
else:
    total=''
    for item in tot:
        total+=str(item)+' '
    print('YES')
    print(total[:-1])
    

