(n, x) = list(map(int, input().split()))
A = tuple(map(int, input().split()))
pre = max(0, A[0] - x)
ans = pre
for i in range(n - 1):
    a = A[i]
    b = A[i + 1]
    a -= pre
    tmp = 0
    if b > x:
        tmp += b - x
        b = x
    if a + b > x:
        tmp += a + b - x
    ans += tmp
    pre = tmp
print(ans)
