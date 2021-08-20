import sys
readline = sys.stdin.readline
T = int(readline())
Ans = ['no'] * T
for qu in range(T):
    (N, K) = list(map(int, readline().split()))
    A = list(map(int, readline().split()))
    A = [-1 if a < K else 0 if a == K else 1 for a in A]
    if 0 not in A:
        continue
    for i in range(1, N - 1):
        if A[i] < 0 and A[i - 1] >= 0 and (A[i + 1] >= 0):
            A[i] = 1
    for i in range(2, N):
        if A[i] < 0 and A[i - 1] >= 0 and (A[i - 2] >= 0):
            A[i] = 1
    for i in range(N - 3, -1, -1):
        if A[i] < 0 and A[i + 1] >= 0 and (A[i + 2] >= 0):
            A[i] = 1
    for i in range(1, N):
        if A[i] == 1 and A[i - 1] == 0:
            A[i] = 0
    for i in range(N - 2, -1, -1):
        if A[i] == 1 and A[i + 1] == 0:
            A[i] = 0
    A.sort()
    if A[-1 - -N // 2] == 0:
        Ans[qu] = 'yes'
print('\n'.join(Ans))
