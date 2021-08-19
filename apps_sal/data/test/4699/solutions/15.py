# 値段、嫌いな数字の数
N, K = map(int, input().split())
# 嫌いな数字
hate_num = list(map(int, input().split()))
# ループ用
i = N

while 1:
    # 支払う金額に入っている数字の抜き出し
    ans = list({int(i) for i in list(str(i))})
    # 支払う金額に嫌いな数字が入っていないか確認
    for j in ans:
        # 嫌いな数字があった時
        if j in hate_num:
            break
    # 嫌いな数字がなかった時
    else:
        print(i)
        break
    i += 1
