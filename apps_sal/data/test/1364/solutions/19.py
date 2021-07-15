N = int(input())
A = [int(a) for a in input().split()]
Type = []
start = 0
leftType = A[0]
end = 0
while end < N:
    if A[end] == leftType: end += 1
    else:
        Type.append(end - start)
        start, leftType = end, A[end]
Type.append(end-start)

maxLength = 0
for i in range(len(Type) - 1):
    maxLength = max(maxLength, min(Type[i], Type[i+1]) * 2)
print(maxLength)

