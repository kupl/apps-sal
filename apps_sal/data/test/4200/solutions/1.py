import bisect
N, M = list(map(int, input().split()))
A = sorted(list(map(int, input().split())))
# print(A,sum(A)/4/M,A[N-M])
if sum(A) / 4 / M <= A[N - M]:
    print('Yes')
else:
    print('No')
