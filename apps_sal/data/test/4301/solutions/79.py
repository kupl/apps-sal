N = int(input())
A = [int(input()) for i in range(N)]

firstVal = max(A)
firstInd = A.index(firstVal)
secondVal = max(A[0:firstInd] + A[firstInd+1:])

for i in range(firstInd):
    print(firstVal)

print(secondVal)

for i in range(N-firstInd-1):
    print(firstVal)

