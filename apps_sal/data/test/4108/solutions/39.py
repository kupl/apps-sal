from collections import Counter

s = input()
t = input()
# sとtの文字列をカウントして昇順にソート
ss = sorted(Counter(s).values())
st = sorted(Counter(t).values())
# アルファベットの種類数と要素数が同じならYes
print("Yes") if ss == st else print("No")
