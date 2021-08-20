"""
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
"""
Yes = 'Yes'
No = 'No'


def main():
    N = int(input())
    up = []
    down = []
    for _ in range(N):
        S = input()
        (h, b) = (0, 0)
        for s in S:
            if s == '(':
                h += 1
            else:
                h -= 1
                b = min(b, h)
        if h >= 0:
            up.append((h, b))
        else:
            down.append((h, b))
    up.sort(key=lambda t: t[1], reverse=True)
    down.sort(key=lambda t: t[0] - t[1], reverse=True)
    H = 0
    for (h, b) in up + down:
        if H + b >= 0:
            H += h
        else:
            print(No)
            return
    if H == 0:
        print(Yes)
    else:
        print(No)


main()
