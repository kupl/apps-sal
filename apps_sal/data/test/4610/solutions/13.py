N, K = map(int, input().split())
A = {}
for i in input().split():
    A[i] = A.get(i, 0) + 1
A = sorted(A.values())
print(sum(A[0:len(A) - K]))
