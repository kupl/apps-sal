N, K = list(map(int, input().split()))
A = [int(a)-1 for a in input().split()]
T = [0] * N
inv = [0] * N
for i in range(N):
    inv[A[i]] = i

L = [a-1 for a in range(N)]
R = [a+1 for a in range(N)]

c = 0
t = 2
i = N-1
while c < N and i >= 0:
    j = inv[i]
    if T[j]:
        i -= 1
        continue
    t = 3 - t
    T[j] = t
    c += 1
    k = K
    pj = j
    while True:
        nj = L[pj]
        if k==0 or nj < 0:
            break
        T[nj] = t
        c += 1
        k -= 1
        pj = nj
    ll = nj
    k = K
    pj = j
    while True:
        nj = R[pj]
        if k==0 or nj >= N:
            break
        T[nj] = t
        c += 1
        k -= 1
        pj = nj
    rr = nj
    if rr < N:
        L[rr] = ll
    if ll >= 0:
        R[ll] = rr
    i -= 1

print("".join(map(str, T)))

