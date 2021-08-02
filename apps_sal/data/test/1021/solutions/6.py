N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
S = [A[i] - A[i - 1] for i in range(1, N)]
T = [B[i] - B[i - 1] for i in range(1, N)]
S.sort()
T.sort()
if A[0] == B[0] and A[N - 1] == B[N - 1] and S == T:
    print('Yes')
else:
    print('No')
