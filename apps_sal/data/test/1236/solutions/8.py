n,k=input().split()
n=int(n)
k=int(k)
s=input()
a=[int(i) for i in s.split()]
nodd=0
for i in a:
    if(i%2!=0):
        nodd+=1
neven=len(a)-nodd
if(n==k):
    if(nodd%2==0):
        print("Daenerys")
    else:
        print("Stannis")
else:
    if(nodd<=int((n-k)/2)):
        print("Daenerys")

    elif(neven<=int((n-k)/2)):
        if(k%2==0):
            print("Daenerys")
        else:
            print("Stannis")
    else:
        if((n-k)%2==0):
            print("Daenerys")
        else:
            print("Stannis")
