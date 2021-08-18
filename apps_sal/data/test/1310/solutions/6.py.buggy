N = int(input())
A = list(int(i) for i in input().split())


def rsq(i, j):
    nonlocal A
    if(i == 0):
        return A[j]
    return A[j] ^ A[i - 1]


for i in range(1, N):
    A[i] = A[i] ^ A[i - 1]

maxv = 0
for i in range(N):
    for j in range(i, N):
        maxv = max(maxv, rsq(i, j))
print(maxv)
