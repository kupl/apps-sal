

n,k=list(map(int,input().split()))
ligne=input()

for i in range(n):
    car=ligne[i]
    if car=="G":
        depart=i
    elif car=="T":
        arrive=i
i=depart
while n>i and (ligne[i]=="." or ligne[i]=="G"):
    i+=k
j=depart

while j>0 and (ligne[j]=="." or ligne[j]=="G"):
    j-=k
    
if j==arrive or i==arrive:
    print("YES")
else:
    print("NO")

