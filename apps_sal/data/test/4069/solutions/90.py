x, k, d = list(map(int, input().split()))

X = abs(x)
if k * d < X:
    ans = X - k * d
else:
    t = X // d  # 絶対値Xを何回D移動すると0になるか
    t_a = k - t  # 0に到達したあとの回数

    if t_a % 2 == 0:
        ans = X % d  # 0に到達したあと偶数ならば往復できるのでその位置から変わらない

    else:
        ans = abs((X % d) - d)
print(ans)
