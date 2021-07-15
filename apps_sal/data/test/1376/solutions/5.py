N = int(input())
A = [int(a) for a in input().split()]
L = [-1] * N
R = [0] * N

for i in range(2*N):
    a = A[i] - 1
    if L[a] < 0:
        L[a] = i
    else:
        R[a] = i

s = L[0]+R[0]
for i in range(N-1):
    s += abs(L[i+1] - L[i]) + abs(R[i+1] - R[i])

print(s)

