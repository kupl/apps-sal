import math
N = int(input())
S = list(input())
A = [0] * N
same = False
for i in range(1, N):
    if S[i] == S[i - 1]:
        same = True
    elif same and S[i] != S[i - 1]:
        A[i] = 1
        same = False
    else:
        same = False
        A[i] = 1

print(sum(A) + 1)
