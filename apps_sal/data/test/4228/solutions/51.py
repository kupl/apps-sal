(N, L) = map(int, input().split())
A = []
for i in range(N):
    A.append(i + L)
if L < 0 and A.count(0) > 0:
    print(sum(A))
elif L < 0:
    print(sum(A[:-1]))
else:
    print(sum(A[1:]))
