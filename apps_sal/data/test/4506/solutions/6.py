n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(n):
    A[i] *= (i + 1) * (n - i)
A.sort()
B.sort(reverse=True)
C = []
cnt = 0
M = 998244353
for i in range(n):
    cnt += A[i] * B[i]
    cnt %= M
print(cnt)

