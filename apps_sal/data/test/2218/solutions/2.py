n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
C = []
U = len(A)
c = 0
g = 0
for i in range(k):
    print(len(C + [A[g]]), ' '.join(map(str, C + [A[g]])))
    g += 1
    if g == len(A):
        g = 0
        C.append(max(A))
        A.remove(max(A))
