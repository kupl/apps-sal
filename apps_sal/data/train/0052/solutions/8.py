n=int(input())
list=[]
summ=int(0)
for i in range(n):
    a=int(input())
    list.append(a)
rev=list[::]
list.sort()
rev.sort(reverse=True)
for x in range(n):
    summ=(summ+((list[x]*rev[x])%10007)%10007)%10007
print(summ)
