N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
x = 0
C = []
D = []
if N == 1:
    print((A[0] + B[0]))
    return
for i in range(N):
    C = A[0:i]
    D = B[i - 1:N]
    x = sum(C) + sum(D)
    ans = max(ans, x)

print(ans)
