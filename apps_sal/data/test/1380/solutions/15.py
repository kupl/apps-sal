n,k=list(map(int,input().split()))

z=[int(x) for x in input().split()]
lim=max(z)
ctr=10000000

minz=[]
minz_num=[]#no. of moves for every element in z
for i in range (1,max(z)+1):
    strt=i
    moves=0
    for j in range (0,len(z)):
        if (z[j]!= strt+j*k):
            moves+=1
    minz.append(moves)
    minz_num.append(strt)



ansf=min(minz)
a=minz_num[minz.index(ansf)]

ans=""
for i in range (0,len(z)):
    if (z[i] > a+ i*k):
        ans+="-"+" "+str(i+1)+" "+str(abs(z[i]-a-i*k))+"\n"
    if (z[i] < a+i*k):
        ans+="+"+" "+str(i+1)+" "+str(abs(z[i]-a-i*k))+"\n"

print (ansf)
print (ans)
        
    

