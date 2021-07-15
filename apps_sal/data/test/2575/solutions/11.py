n=int(input())
z=[]
for i in range (0,n):
    x=int(input())
    n=360/(180-x)
    z.append(n)

for j in range (0,len(z)):
    if (int(z[j])==z[j]):
        print("YES")
    if (int(z[j]) !=z[j]):
        print ("NO")


