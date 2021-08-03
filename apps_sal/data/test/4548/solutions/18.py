import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
A = list(map(int, input().split()))
if A[int(M / 2)] > X:
    b = [i for i in A if i < X]
else:
    for i in A[::-1]:
        b = [i for i in A if i > X]

print(min(len(b), M - len(b)))
