# cook your dish here
t=int(input())
n=list(map(int,input().split()[:t]))
for i in n:
    li=[3]
    li1=3
    list1=[1]
    list2=[2]
    list3=[4]
    list4=[3]
    l1=1
    l2=2
    l3=4
    l4=3
    for j in range(i-1):
        li.append(li1*2)
        li1=li1*2
    for i in range(i-1):
        list1.append(l1+li[i])
        l1=l1+li[i]

        list2.append(l2+li[i])
        l2=l2+li[i]

        list3.append(l3+li[i+1])
        l3=l3+li[i+1]
        list4.append(l4+li[i])
        l4=l4+li[i]
    for i in (list1):
        print(i,end=" ")
    print()
    for i in (list2):
        print(i,end=" ")
    print()
    for i in (list3):
        print(i,end=" ")
    print()
    
    for i in (list4):
        print(i,end=" ")
    print()


