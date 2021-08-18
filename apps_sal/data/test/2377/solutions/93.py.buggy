import sys

n, h = map(int, input().split())

max_a = 0
b = []
for i in range(n):
    x, y = map(int, input().split())
    max_a = max(max_a, x)
    b.append(y)

# 投げる価値がある刀を抜粋する
b = [x for x in b if x > max_a]

# 強い順に投げていく
b.sort(reverse=True)

i = 0
if len(b) > 0:
    for i, x in enumerate(b):
        i += 1
        h -= x
        if h <= 0:
            print(i)
            return

# 投げ終わったら最強の刀で攻撃し続ける
print((h + max_a - 1) // max_a + i)
