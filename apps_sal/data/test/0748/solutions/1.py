import sys
N=int(sys.stdin.readline())

A=list(map(int,sys.stdin.readline().split()))



L=[0]*8

for item in A:
    L[item]+=1

if(L[1]!=(N//3)):
    print(-1)

elif(L[7]>0 or L[5]>0):
    print(-1)

elif(L[3]+L[2]!=(N//3)):
    print(-1)

elif(L[4]+L[6]!=(N//3)):
    print(-1)

elif(L[2]<L[4]):
    print(-1)

else:
    for i in range(L[3]):
        sys.stdout.write("1 3 6\n")
    L[6]-=L[3]
    for i in range(L[6]):
        sys.stdout.write("1 2 6\n")
    for i in range(L[4]):
        sys.stdout.write("1 2 4\n")
        

