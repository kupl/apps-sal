N, K = [int(n) for n in input().split()]
A = [int(n) for n in input().split()]
E = [0] * N

Elist = {}
for val in set(A):
    e = 0
    for i in range(1, val + 1):
        e += i / val
    Elist[val] = e

for i in range(N):
    E[i] = Elist[A[i]]


En = sum(E[:K])
Emax = En
for j in range(1, N - K + 1):
    En = En - E[j - 1] + E[j - 1 + K]
    Emax = max(Emax, En)

print(Emax)
