import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, abs(A[i] - A[j]))
print(ans)
