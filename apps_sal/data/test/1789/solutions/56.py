
#標準入力
s = list(map(int, input().split()))

a = int(s[0])
b = int(s[1])
x = int(s[2])
y = int(s[3])

move_withoutstep_1 = 9999999999
move_withoutstep_2 = 9999999999

#階段移動を使わない場合の移動時間
# a > bの時
if a > b:
    move_withoutstep_1 = ((a-b)-1)*x + (a-b)*x
#a < bの時
elif a <= b:
    move_withoutstep_2 = ((b-a)+1)*x + (b-a)*x


#階段移動を使う場合の移動時間
move_upstairs = 9999999999
move_downstairs = 9999999999

if a < b:
    move_upstairs = (b-a)*y + x
elif a > b:
    #最後の下りはななめ移動（廊下を使った移動）の方が早いので、それを考慮して階段移動の回数を1回分減らす。
    #x+yよりもxの方が小さいのは条件より自明。
    move_downstairs = (a-b-1)*y + x

#print(move_withoutstep_1,move_withoutstep_2,move_upstairs,move_downstairs,move_downstairs_2)
print((min(move_withoutstep_1,move_withoutstep_2,move_upstairs,move_downstairs)))

