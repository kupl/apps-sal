import sys
input = sys.stdin.readline
n = int(input())
A = [0] + list(map(int, input().split()))
ANS = 0
for i in range(1, n + 1):
    if A[i] > A[i - 1]:
        ANS += (n - A[i] + 1) * (A[i] - A[i - 1])
    else:
        ANS += A[i] * (A[i - 1] - A[i])
print(ANS)
