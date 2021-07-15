N, M = map(int, input().split())

#N人の参加者から、M組選ぶ
#これをNセット実施。
#組合わせの距離が重複しなければ、成立


#参加者を半分に分け、
#前半を距離奇数、後半を距離偶数にする

#参加者を半分に分ける
div_point=int((N/2))
#前半グループを奇数にする
if div_point%2==0:
    div_point-=1
#後半グループは更に半分に分ける
re_point=div_point+int((N-div_point)/2)

#組を作る
i=0 #初期化
while 1<div_point-i*2 and i<re_point and i<M:#前半グループ・・・距離が奇数になるように組み分け
    ent1=i+1 #前半グループ：一人目
    ent2=div_point-i #前半グループ：二人目
    print(str(ent1) + ' ' + str(ent2))
    i+=1
for j in range(M-i):#後半グループ
    ent1=re_point-j #後半グループ：一人目
    ent2=re_point+j+1 #後半グループ：二人目
    print(str(ent1) + ' ' + str(ent2))
