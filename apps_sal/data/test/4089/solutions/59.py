n = int(input())
l = "Xabcdefghijklmnopqrstuvwxyz"
ans = ""
while True:
    # あまりを文字に変換する
    # あまりをdに代入する
    d = n % 26
    if d == 0:
        d = 26
    ans += l[d]

    # あまりをnから引いて、次の桁へ
    n -= d

    # nが0だったら終了
    if n == 0:
        break

    # nの更新
    n //= 26

print(ans[::-1])
