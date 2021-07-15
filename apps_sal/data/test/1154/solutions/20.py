d=input().split()
d=[int(x) for x in d]
n,h,k=d[0],d[1],d[2]
d=input().split()
d=[int(x) for x in d]
S=0
R=0
for i in d:

    if R+i<=h:
        S+=i//k
        R+=i%k 
    else:
        while R+i>h:
            if R%k==0:
                S+=R//k
                R=0
            elif R<k:
                S+=1
                R=0
            else:
                S+=R//k
                R=R%k
        S+=i//k
        R+=i%k
      
if R%k==0:
    S+=R//k
else:
    S+=R//k
    S+=1
print(S)

