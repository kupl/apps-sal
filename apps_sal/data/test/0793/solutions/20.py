N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

A = []
B = []
mod = 10**9 + 7

for i in range(N):
    if S[i] in T:
        A.append(S[i])

for i in range(M):
    if T[i] in S:
        B.append(T[i])

l1 = [1] * (N + 1)

for i, t in enumerate(T):
    l2 = l1[:]
    k = 0
    for j, s in enumerate(S):
        if t == s:
            k += l1[j]
        l2[j + 1] = (l1[j + 1] + k) % mod
    l1 = l2
print(l1[-1])
