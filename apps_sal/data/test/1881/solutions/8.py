N, K = input().split()
N, K = int(N), int(K)
P = [int(x) for x in input().split()]
A = [None]*256
A[0] = 0
for i in range(N):
    pn = P[i]
    if A[pn] is None:
        for j in range(K-1, -1, -1):
            if pn < j: continue
            if A[pn-j] is None:
                A[pn-j] = pn-j
                break
            else:
                if A[pn-j] + K - 1 >= pn:
                    break
        for jj in range(j, -1, -1):
            A[pn-jj] = A[pn-j]
print(*[A[P[i]] for i in range(N)])

