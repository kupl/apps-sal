n, k = list(map(int, input().split()))
h = list(map(int, input().split()))

# モンスターの数より使える必殺技の数が多ければおわり
if n <= k:
    print((0))
    return

num = 0
# 降順にソート
h.sort(reverse=True)
# 大きい数順に必殺技を使う
# 残ったやつを数える
for i in h[k:]:
    num += i

print(num)

