import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    tmp = sum(A[:i + 1]) + sum(B[i:])
    ans = max(ans, tmp)
print(ans)
