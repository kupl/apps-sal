N=int(input())
H=list(map(int,input().split()))
for i in range(N-1):
    if H[i]>H[i+1]+1:
        print("No")
        break
    elif H[i]==H[i+1]+1:
        H[i]-=1
        H[i+1]+=1
else:
    print("Yes")

