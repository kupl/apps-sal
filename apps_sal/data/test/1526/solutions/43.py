A = list(map(int,input().split()))
A.sort(reverse=True)
X = (A[0]-A[1])+(A[0]-A[2])
print(X//2+2*(X%2))
