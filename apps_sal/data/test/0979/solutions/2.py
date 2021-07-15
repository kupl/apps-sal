N, M = list(map(int, input().split()))
A = sorted([int(a) for a in input().split()])

if N > M:
    print(0)
else:
    s = 1
    for i in range(N):
        for j in range(i):
            s = s * (A[i] - A[j]) % M
    print(s)

