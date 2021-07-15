N = int(input())
A = [int(d) for d in input().split()]

S = []
X = 0
for i in range(N):
    if X < A[i]:
        X = A[i]
    else:
        pass
    S.append( X - A[i] )

print(sum(S))
