
N, M = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
for x in A:
    n = x.pop(0)
I = set(A[0])
for i in range(1, N):
    I = I.intersection(A[i])
print((len(I)))
