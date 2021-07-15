N, K = map(int, input().split())
A = [0]+list(map(int, input().split()))
B = [-1]*-~N
p = 1
for i in range(K):
    if B[p] >= 0 :break
    B[p] = i
    p = A[p]
else: print(p); return
print(B.index((K-B[p])%(i-B[p])+B[p]))
