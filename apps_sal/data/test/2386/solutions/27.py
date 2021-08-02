import sys

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))

for i in range(N):
    A[i] = A[i] - (i + 1)

A.sort()
b = A[(N - int(N % 2 == 0)) // 2]

res = 0
for a in A:
    res += abs(a - b)

print(res)
