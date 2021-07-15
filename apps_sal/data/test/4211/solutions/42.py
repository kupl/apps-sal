N = int(input())
B = list(map(int, input().split()))
A = [B[0], B[0]]
for i in range(1, N-1):
    b = B[i]
    A.append(b)
    a = max([A[i],A[i+1]])
    if a > b:
        A[A.index(a)] = b
print((sum(A)))

