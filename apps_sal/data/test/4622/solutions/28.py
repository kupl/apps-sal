N = int(input())
A = sorted([int(i) for i in input().split()])
for i in range(N-1):
    if(A[i] == A[i+1]):
        print("NO")
        return
print("YES")
