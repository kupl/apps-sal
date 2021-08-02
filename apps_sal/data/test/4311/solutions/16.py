s = int(input())
a = [s]
i = 0
while True:
    i = i + 1
    # 前回の値によって計算を変える。
    if a[i - 1] % 2 == 0:
        n = a[i - 1] // 2
    else:
        n = 3 * a[i - 1] + 1
    # 数列に同じ値が含まれているかどうか？
    if n in a:
        # 配列が0から始まるため、カウントアップ。
        print((i + 1))
        break
    a.append(n)
