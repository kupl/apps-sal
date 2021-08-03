import sys
input = sys.stdin.readline
n, k = list(map(int, input().split()))
A = [int(i) for i in input().split()]
B = []
for i in range(1, n):
    B.append(A[i] - A[i - 1])
B.sort()
print(sum(B[:n - k]))
