# モンスターの体力H
# アライグマの必殺技の種類N
# i番目の必殺技使うと、モンスターの体力Ai減らせる

# H - (A1 + A2 + A3...) <= 0 となるなら 'Yes',
# ならないなら'No'が出力される

h, n = map(int, input().split())
damage = list(map(int, input().split()))

if h - sum(damage) <= 0:
    print("Yes")
else:
    print("No")
