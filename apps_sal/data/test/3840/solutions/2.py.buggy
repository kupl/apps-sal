n = int(input())
if n == 1 or n % 2 == 0:
    print(-1)
    return
A = [0] * (n + 1)
A[1:n + 1] = list(map(int, input().split()))
ans = 0
for i in range(n, 0, -1):
    if(A[i] <= 0):
        continue
    x = int(i / 2)
    A[x] -= A[i]
    ans += A[i]
    if i % 2 == 1:
        A[i - 1] -= A[i]
    A[i] = 0
print(ans)
