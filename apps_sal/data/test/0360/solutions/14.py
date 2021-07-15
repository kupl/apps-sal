n=int(input())
tot=[]
for i in range(n):
    a,b=[int(x) for x in input().split()]
    tot.append((a,b))
k=int(input())
counter=0
for item in tot:
    if item[0]<=k<=item[1]:
        print(n-counter)
        break
    counter+=1

