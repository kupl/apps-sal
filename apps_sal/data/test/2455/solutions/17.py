T=int(input())

while T>=1:
    T-=1
    a=input()
    list=[]
    for i in range(1,13):
        if 12 % i==0:
            l=12//i
            for j in range(0,l):
                for k in range(0,i):
                    if a[k*l+j]!='X':
                        break
                else:
                    break
            else:
                continue
            list.append(i)
    print(len(list),end=' ')
    for i in range(0,len(list)):
        print(str(list[i])+'x'+str(12//list[i]),end=' ')
    print()

