n, k = map(int, input().split())

if k % 2 == 1:  # kが奇数の場合
    x = 0
    for i in range(1, n + 1):
        if i % k == 0: x += 1  # kで割り切れる値の数をカウント
    print(x**3)  # 組み合わせ分増える
else:  # kが偶数の場合
    x = 0
    for i in range(1, n + 1):
        if i % k == 0: x += 1  # kで割り切れる値の数をカウント
    y = 0
    for i in range(1, n + 1):
        if i % k == k // 2: y += 1  # k//2で割り切れる値の数をカウント
    print(x**3 + y**3)  # 組み合わせ分増える
