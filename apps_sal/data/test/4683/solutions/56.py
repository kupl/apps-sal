from sys import stdin
N = int(stdin.readline().rstrip())
A = [int(_) for _ in stdin.readline().rstrip().split()]
sa = sum(A)
ans = 0
for i in range(N):
    sa -= A[i]
    ans += A[i] * sa
    ans %= 10 ** 9 + 7
print(ans)
