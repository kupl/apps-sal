(x, k, d) = list(map(int, input().split()))
X = abs(x)
if k * d < X:
    ans = X - k * d
else:
    t = X // d
    t_a = k - t
    if t_a % 2 == 0:
        ans = X % d
    else:
        ans = abs(X % d - d)
print(ans)
