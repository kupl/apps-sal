'''
○ 基本方針
'(' を1上昇、')'を1下降とイメージすると、
この問題は「0未満にならず、最終的に0になるか」と言い換えられる。

1. ／ 型
2. V 型で上昇
3. V型で下降
4. ＼型
の順で使えばよい。

2は、V字の最下点が最も高いものから使うのが最適。（徐々に、大きく沈み込むものを使えるようになる）
3は、(|下降| - V字の最下点) が最も大きいものから使うのが最適。（沈み込みが大きいものは早めに消化する）

ここで、1は2、3は4と合わせて考えて良い。
'''

Yes = 'Yes'
No = 'No'

def main():
    # 入力
    N = int(input())
    up = []     # 上昇が0以上のもの
    down = []   # 上昇が0未満のもの
    for _ in range(N):
        S = input()
        h, b = 0, 0 # h:上昇数、b:最下点
        for s in S:
            if s=='(':
                h += 1
            else:
                h -= 1
                b = min(b, h)
        #
        if h>=0:
            up.append((h, b))
        else:
            down.append((h, b))
    # 演算
    up.sort(key=lambda t: t[1], reverse=True)           # 上昇は、最下点が高いものから使う
    down.sort(key=lambda t: t[0]-t[1], reverse=True)    # 下降は、沈み込み後の反転上昇が大きいものから使う
    H = 0   # 現在の高さ
    for h, b in up + down:
        if H+b>=0:  # 高さが0未満にならない条件
            H += h
        else:
            print(No)
            return
    # 出力
    if H == 0:
        print(Yes)
    else:
        print(No)


main()


