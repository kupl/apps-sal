N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

count = 0
for j in A:
    count += B[j-1]

#print(count)

for z in range(N-1):
    if A[z+1]- A[z] == 1:
        zz = A[z]
        count += C[zz-1]

print(count)
    
    

