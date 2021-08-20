N = int(input())
A = list(map(int, input().split()))
Q = int(input())
C = (10 ** 5 + 1) * [0]
T = sum(A)
for a in A:
    C[a] += 1
for q in range(Q):
    (b, c) = map(int, input().split())
    T += C[b] * (c - b)
    C[c] += C[b]
    C[b] = 0
    print(T)
