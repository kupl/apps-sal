N = int(input())
P = list(map(int, input().split()))

I = [0] * N
for i in range(N):
    I[P[i]-1] = i

ans = 0
L = [i for i in range(-1, N-1)]
R = [i for i in range(1, N+1)]

for p in range(1,N+1):
    i = I[p-1]

    if R[i] < N:
        L[R[i]] = L[i]
    if L[i] >= 0:
        R[L[i]] = R[i]

    l1 = L[i]
    l2 = L[l1] if l1 >= 0 else -1
    r1 = R[i]
    r2 = R[r1] if r1 < N else N
    ans += p * ((r1-i)*(l1-l2) + (i-l1)*(r2-r1))

print(ans)

