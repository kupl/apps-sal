import sys
input = sys.stdin.readline
(N, M, X) = list(map(int, input().split()))
A = list(map(int, input().split()))
count = 0
if A[int(M / 2)] > X:
    for i in A:
        if i < X:
            count += 1
        else:
            break
else:
    for i in A[::-1]:
        if i > X:
            count += 1
        else:
            break
print(min(count, M - count))
