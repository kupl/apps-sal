N=int(input())
BA=[]
for _ in range(N):
    A,B=list(map(int,input().split()))
    BA.append([B,A])
BA.sort()
T=0
for i in range(N):
    T+=BA[i][1]
    if T>BA[i][0]:
        print("No")
        break;
else:
    print("Yes")

