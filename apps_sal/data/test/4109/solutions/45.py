# ABC167
N, M, X = map(int, input().split())
c = []  # 参考書の値段
a = []  # 各参考書に入る理解度
for i in range(N):
    c_temp, *a_temp = list(map(int, input().split()))  # こうすると、2つ目以降をリストで受け取れる
    c.append(c_temp)
    a.append(a_temp)
price_min = 10000000
for i in range(2**N):
    price_total = 0  # 値段の合計
    learn_total = [0] * M  # 理解度の合計
    for j in range(N):
        if (i >> j) & 1:  # j桁目が0か1か見て、j冊目を買うか買わないか判定します
            price_total += c[j]  # 買うので、j冊目の値段を加算します
            learn = a[j]  # 「j冊目の参考書を読んで増える、各アルゴリズムの理解度」のリストです
            for k, la in enumerate(learn):  # 理解度を加算します enumerateを使うと、range(n)よりスマートです
                learn_total[k] += la
    if all(learn_total[k] >= X for k in range(M)):
        if price_min > price_total:
            price_min = price_total

if price_min == 10000000:
    print(-1)
else:
    print(price_min)
