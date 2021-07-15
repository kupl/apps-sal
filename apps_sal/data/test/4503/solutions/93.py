# モンスターの体力は H
# アライグマは N 種類の必殺技を使うことができ
# i番目の必殺技を使うとモンスターの体力を Ai 減らすことができます。
# モンスターの体力を0以下にすれば、アライグマ勝ち
# アライグマが同じ必殺技を 2 度以上使うことなくモンスターに勝つことができるなら Yes を、
# できないなら No を出力してください。

H, N = list(map(int, input().split()))
data = list(map(int, input().split()))

if H - sum(data) > 0:
    print('No')
else:
    print('Yes')

