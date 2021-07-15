N=int(input())
list1 = list(map(int, input().split()))

list2=[]
for i in list1:
    if i%2==0:
        list2.append(i)
    else:
        continue

list3=[]
for j in list2:
    if j%3==0 or j%5==0:
        list3.append(j)
    else:
        continue

x=len(list2)
y=len(list3)

if x==y:
    print('APPROVED')
else:
    print('DENIED')

