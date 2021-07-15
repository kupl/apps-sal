N = int(input())
A = list(map(int, input().split()))
x = A[0]
y = sum(A[1:])
ans = abs(x - y)
for i in range(1, N - 1):
    a = A[i]
    x += a
    y -= a
    dif = abs(x - y)
    if dif < ans:
        ans = dif
print(ans)
