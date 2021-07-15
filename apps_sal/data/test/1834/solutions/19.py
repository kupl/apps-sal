n=int(input())
mas=[int(x) for x in input().split()]
mas.sort()
k=0
l=n-1
for i in range(n):
    if i&1:
        print(mas[l],end=' ')
        l-=1
    else:
        print(mas[k],end=' ')
        k+=1
