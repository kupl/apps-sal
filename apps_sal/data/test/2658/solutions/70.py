N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = [0] * (N + 1)
B[0] = 1
c = 0
d = 0
if B[0] in A:
    c = B[0]
for i in range(1, N + 1):
    B[i] = A[B[i - 1] - 1]
#  if c==B[i]:break
#  if A.count(B[i])>1 and d==0:c=B[i];d+=1

d = B.index(B[-1]) + 1
# print(B.index(B[N-1]))

# print(B,d)
# print(d+1+(K-d-1)%(N-d-1))
# print(B[K],K,d,(K+1-d),(N+1-d))
if K <= N:
    print((B[K]))
    return
if (K + 1 - d) % (N + 1 - d) == 0:
    print((B[-1]))
else:
    print((B[d - 1 + (K + 1 - d) % (N + 1 - d)]))
# print(B[d+1+(K-d-1)%(N-d-1)]-1)
