N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C=[]
for i in range(N):
    C.append(sum(A[0:i+1])+sum(B[i:]))
print(max(C))
