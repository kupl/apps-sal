from numpy import*
N, M, *U = map(int, open(0).read().split())
p = ones(M + 1)
for s in U[:N]:
    p[1:] = ((p[:-1] * (s == array(U[N:]))).cumsum() + p[1:]) % (10**9 + 7)
print(int(p[-1]))
