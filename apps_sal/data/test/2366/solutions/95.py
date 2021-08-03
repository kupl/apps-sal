import collections
N = int(input())
A = list(map(int, input().split()))

D = collections.Counter(A)
s = 0
for i in D:
    s += D[i] * (D[i] - 1) // 2

for i in range(N):
    print(s - (D[A[i]] - 1))
