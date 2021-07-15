n=int(input())
days=input().split()
for i in range (n):
    days[i]=int(days[i])
works=True
for i in range (n):
    if days[i]<0:
        works=False
        break
    if days[i]%2==1:
        if i==n-1:
            works=False
            break
        else:
            days[i+1]-=1
if works:
    print ("YES")
else:
    print ("NO")

