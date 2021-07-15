#このプログラムはpypyじゃ通らない
import collections,math
s = input()
t = input()
#tを構成文字で、sにない文字があったらダメ。
#構成できるなら最大でもlen(t)個しかないから、10^100の連結は必要ない

#最も不足する文字を探す
ls = collections.Counter(s)
lt = collections.Counter(t)

time_dict ={}
tmp=0
max_time=0#一番少ないやつ
for t_key,t_val in list(lt.items()):
    if t_key not in ls:#sの中にtの文字がない
        print((-1))
        return

#文字をカウントしていく
cnt = 0
tt = list(t[::-1])#指定したい文字へのアクセス時間を1にしたいので反転
idx=0
ss = s#ssは検索文字列
while tt!=[]:#ttが空っぽになったらおしまい
    next_t = tt.pop()#つぎに構成したい文字= next_t
    idx=ss.find(next_t)#検索文字列にnext_tがあるか
    if idx == -1:#ない
        cnt += len(ss)#検索文字列の長さを全部足す
        idx = s.find(next_t)#新たにsを検索文字列として探す
        ss = s[idx+1:]#next_t以降の文字列を次回の検索文字列をセット
        cnt += idx+1 #nex_tが見つかった文字までの長さ
    else:#ある
        cnt += idx+1 #文字長さを足す 
        ss = ss[idx+1:]#次回の検索文字列をセット
print(cnt)

