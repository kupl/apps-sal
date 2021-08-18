n, m = input().split()
n, m = int(n), int(m)
A = input().split()
A = [int(ai) for ai in A]
A.sort()

D = []
for i, a in enumerate(A):
    if i < m:
        D.append(A[i])
    else:
        D.append(A[i] + D[i - m])

P = [D[0]]
for i in range(1, n):
    P.append(P[-1] + D[i])

print(' '.join([str(pi) for pi in P]))
