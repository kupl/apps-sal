from collections import Counter
N = int(input())
A = list(map(int, input().strip().split()))
Q = int(input())
B = [0] * Q
C = [0] * Q
K = Counter(A)
ans = 0

for i in range(Q):
    B[i], C[i] = list(map(int, input().split()))


for i in K:
    ans += i * K[i]

for i in range(Q):
    ans -= B[i] * K[B[i]]
    ans += C[i] * K[B[i]]
    K[C[i]] += K[B[i]]
    K[B[i]] = 0
    print(ans)
