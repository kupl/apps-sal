import collections
N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
Q = int(input())
B = [0] * Q
C = [0] * Q
for i in range(Q):
    (B[i], C[i]) = map(int, input().split())
D = collections.Counter(A)
s = sum(A)
for i in range(Q):
    s = s - B[i] * D[B[i]]
    D[C[i]] += D[B[i]]
    s = s + C[i] * D[B[i]]
    D[B[i]] = 0
    print(s)
