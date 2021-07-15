N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

from collections import Counter

cA = Counter(A)
cB = Counter(B)

f = 0

for num, val in cA.items():
    if num not in cB:
        continue
    else:
        if cB[num] + val > N:
            f = 1

tpA = [-1] * (N + 1)
tpB = [-1] * (N + 1)
a = A[0]
b = B[0]
tpB[b] = 0
for i in range(1, N):
    if a != A[i]:
        tpA[a] = i
        a = A[i]
    if b != B[i]:
        b = B[i]
        tpB[b] = i
tpA[a] = N


ans = [0] * N
if f == 1:
    print("No")
else:
    print("Yes")
    t = 0
    for i in range(N+1):
        if tpA[i] >= 0 and tpB[i] >= 0:
            t = max(t, tpA[i] - tpB[i])
    for i in range(N):
        ans[i+t-N] = B[i]
    #print(tpA, tpB, t)
    print(" ".join([str(_) for _ in ans]))
