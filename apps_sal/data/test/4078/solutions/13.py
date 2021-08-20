(n, m) = list(map(int, input().split()))
A = [int(a) for a in input().split()]
L = [0] * m
R = [0] * m
for i in range(m):
    (l, r) = list(map(int, input().split()))
    L[i] = l - 1
    R[i] = r - 1
ma = -1
mai = -1
for i in range(n):
    B = [a for a in A]
    for j in range(m):
        if L[j] > i or R[j] < i:
            for k in range(L[j], R[j] + 1):
                B[k] -= 1
    d = B[i] - min(B)
    if d > ma:
        ma = d
        mai = i
print(ma)
B = [a for a in A]
X = []
for j in range(m):
    if L[j] > mai or R[j] < mai:
        X.append(str(j + 1))
print(len(X))
print(' '.join(X))
