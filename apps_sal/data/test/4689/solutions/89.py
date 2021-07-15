K, N = list(map(int,input().split()))
A    = list(map(int,input().split()))
A.sort()
d = [A[i+1]-A[i] for i in range(N-1)]
d.append(A[0]+K-A[-1])
print(K-max(d))
