n, q = map(int, input().split())
S = input()
*LR, = (map(int, input().split()) for _ in range(q))

A = [0] * n
for i in range(1, n):
    A[i] = A[i - 1] + (S[i - 1:i + 1] == 'AC')
for l, r in LR:
    print(A[r - 1] - A[l - 1])
