N = int(input())
K = int(input())

out = 1
flg = 0
for i in range(N):  # Aの回数を数えるためのループ
    if not flg:  # フラグが立ってなかったら操作A
        out *= 2
        if out > K:
            flg = 1
    else:  # フラグが立ったら操作B
        out += K

print(out)
