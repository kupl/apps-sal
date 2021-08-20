(N, M) = list(map(int, input().split()))
A = sorted([int(a) for a in input().split()])
B = [a for a in A]
for i in range(M, N):
    B[i] = B[i - M] + A[i]
s = 0
ANS = []
for i in range(N):
    s += A[i]
    if i >= M:
        s += B[i - M]
    ANS.append(s)
print(*ANS)
