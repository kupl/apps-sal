import sys
N = int(input())
A = list(map(int, input().split()))
A.sort()
A.reverse()
ans = 0
for i in range(N // 2):
    ans += A[i]
for i in range(N - N // 2 - 1):
    ans += A[i + 1]
print(ans)
