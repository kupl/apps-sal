N = int(input())
A = [int(x) for x in input().split()]
B = [A[0]]
for i in range(len(A)):
    if B[i] > A[i]:
        B[i] = A[i]
    B.append(A[i])
print(sum(B))
