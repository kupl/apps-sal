Sd = input()
T = input()
#Sdの?以外の文字のインデックスを取得
indexes = []
for i in range(len(Sd)):
    if Sd[i] != "?":
        indexes.append(i)

t0 = 0#tの先頭位置
S_list = []
while t0 <= (len(Sd)-len(T)):
    flg = 0
    tmp_S = Sd[:t0] + T + Sd[t0+len(T):]

    #条件1を満たすかどうかのチェック
    for index in indexes:
        if Sd[index] != tmp_S[index]:#Sdと一致していなかったら
            flg = 1
    if flg:#flgが立った文字列は条件を満たさないためスキップ
        t0 += 1
        continue

    #?にaを積めてリストに格納
    tmp_S = tmp_S.replace('?', 'a')
    S_list.append(tmp_S)
    t0 += 1

if not S_list:
    print("UNRESTORABLE")
    return

S_list.sort()#辞書式にソート
print(S_list[0])
