N = int(input())
A = list(map(int,input().split()))
A.append(0)
A.insert(0,0)
S = 0

for i in range(len(A)-1):
    S+=abs(A[i+1]-A[i])#総コスト
    
for i in range(1,N+1):
    print((S-abs(A[i]-A[i-1])-abs(A[i+1]-A[i])+abs(A[i+1]-A[i-1])))




