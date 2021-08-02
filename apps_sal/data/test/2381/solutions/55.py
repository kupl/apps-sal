import numpy as np
N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7
if N == K:
    ans0 = 1
    for a in A[0:N]:
        ans0 *= a
        ans0 %= MOD
    print(ans0)
    return
A = sorted(A)
if (K % 2 == 1 and A[-1] < 0):
    ans1 = 1
    for a in A[N - K:N]:
        ans1 *= a
        ans1 %= MOD
    print(ans1)
    return

A = sorted(A, key=lambda x: abs(x), reverse=True)
AA = [np.sign(i) for i in A]

ansA = 1
for a in A[0:K]:
    ansA *= a
    ansA %= MOD
ansAA = AA[0:K].count(-1) % 2
if ansA == 0 or ansAA == 0:
    print(ansA)
    return

while ansA > 0:
    ansA -= MOD

B1 = A[0:K]
C1 = A[0:K]
B2 = sorted(A[K:N])
Bp = [i for i in A[0:K] if i > 0]
Bm = [i for i in A[0:K] if i < 0]

if B2[0] > 0: B2.insert(0, 0)
if B2[-1] < 0: B2.insert(-1, 0)
if not Bp: Bp.insert(0, B1[-1])
if not Bm: Bm.insert(0, B1[0])

# print(Bp,Bm,B2)
# print(Bp[-1],B2[0])
B1.remove(Bp[-1])
B1.append(min(B2[0], 0))
# print(B1)
ansB = 1
for a in B1[0:K]:
    ansB *= a
    ansB %= MOD
# print(Bm[-1],B2[-1])
C1.remove(Bm[-1])
C1.append(max(B2[-1], 0))

ansC = 1
for a in C1[0:K]:
    ansC *= a
    ansC %= MOD
# print(B1,C1)
# print(ansB,ansC)
BB1 = [np.sign(i) for i in B1]
ansBB1 = BB1[0:K].count(-1) % 2
BB2 = [np.sign(i) for i in C1]
ansBB2 = BB2[0:K].count(-1) % 2
# print(ansBB1,ansBB2)
if ansBB1 == 1:
    print(ansC)
    return
if ansBB2 == 1:
    print(ansB)
    return
# print(B2[0]/Bp[-1],B2[-1]/Bm[-1])
# print(Bp[-1]*B2[-1],Bm[0]*B2[0])

# print(abs(Bp[-1]*B2[-1])-abs(Bm[-1]*B2[0]))
# print(ansB,ansC)
if abs(Bp[-1] * B2[-1]) - abs(Bm[-1] * B2[0]) >= 0:
    print(ansC)
else: print(ansB)
