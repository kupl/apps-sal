n=int(input())
a=[int(el) for el in input().split()]
k0=0
kotr=0
index_minotr=0
minotr=float('-inf')
minotr_index=-1
minabs=float('+inf')
minabs_index=-1
index0=-1
for i in range (n):
    if a[i]==0:
        k0+=1
        index0=i
    else:
        if abs(a[i])<minabs:
            minabs=abs(a[i])
            minabs_index=i
    if a[i]<0:
        kotr+=1
        if a[i]>minotr:
            minotr=a[i]
            minotr_index=i



if k0==n-1 and kotr==0:
    for i in range (n-1):
        for j in range (i+1,n):
            if a[i]==0 and a[j]==0:
                print(1,i+1,j+1)
                index0=j
#                a[i]=1
                break
    print(2, index0+1)
    raise SystemExit()

if (k0==n-1 and kotr==1) or k0==n:
    i=0
    for i in range(n-1):
        print(1,i+1,i+2)
    raise SystemExit



if kotr%2==0:
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]==0 and a[j]==0:
                print(1,i+1,j+1)
                index0=max(index0,j)
                break
            if a[i]!=0 and a[j]!=0:
                print(1,i+1,j+1)
                break
    if index0!=-1:
        print(2,index0+1)
    raise SystemExit

#кол-во отрицательных нечетно
#перемножаем все нули с минимальным нечетным и удаляем


for i in range(n-1):

    for j in range(i+1,n):

        if a[i]==0 and a[j]==0:
            print(1,i+1,j+1)
            index0=max(index0,j)
            break
        if a[i]==0 and j==minotr_index:
            print(1,i+1,j+1)
            index0=max(index0,j)
            a[j]=0
            break
        if i==minotr_index and a[j]==0:
            print(1,i+1,j+1)
            index0=max(index0,j)

            break
        if i!=minotr_index and j!=minotr_index and a[i]*a[j]!=0:
            print(1,i+1,j+1)
            break


if index0==-1:
    print(2,minotr_index+1)
else:
    print(2,index0+1)




