from numpy import*
N, M, *U = map(int, open(0).read().split())
T = array(U[N:])
p = ones(M + 1)
for s in U[:N]: p[1:] = ((p[:-1] * (s == T)).cumsum() + p[1:]) % (10**9 + 7)
print(int(p[-1]))
