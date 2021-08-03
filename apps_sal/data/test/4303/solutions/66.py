n, k = map(int, input().split())
x = list(map(int, input().split()))
ans = 10**10
for i in range(n - k + 1):
    a = x[i + k - 1]
    b = x[i]
    if a < 0:
        ans = min(ans, abs(b))
    else:
        if b < 0:
            ans = min(ans, min(a, abs(b)) * 2 + max(a, abs(b)))
        else:
            ans = min(ans, a)
print(ans)
