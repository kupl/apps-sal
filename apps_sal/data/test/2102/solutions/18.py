la = input().split()
la = list(map(int,la))
t=input()
lb = input().split()
lb = list(map(int,lb))
lenb=len(lb)
l=[(lb[j]-i,j) for i in la for j in range(lenb)]
l.sort()
last=0
first=0

l0=[0]*lenb
l1=[i for i in range(lenb)]
dic=dict(list(zip(l1,l0)))
dic[l[first][1]]+=1
length=1
lenl=len(l)
while (length<lenb):
    last+=1
    if dic[l[last][1]]==0:
        length+=1
    dic[l[last][1]]+=1

minnum=l[last][0]-l[first][0]
t=0
while (1):
    dic[l[first][1]] -= 1
    while dic[l[first][1]]!=0:

        first += 1
        dic[l[first][1]]-=1

        if minnum > l[last][0] - l[first][0]:
            minnum = l[last][0] - l[first][0]
        if first == last:
            break
    first+=1
    last+=1
    if last>=lenl:
        break
    while dic[l[last][1]]!=0:
        dic[l[last][1]] += 1
        last=last+1
        if last >= lenl:
            break

    if last>=lenl:
        break
    dic[l[last][1]] += 1

    if minnum>l[last][0]-l[first][0]:
        minnum = l[last][0] - l[first][0]
    if minnum==0:
        break



print(minnum)






