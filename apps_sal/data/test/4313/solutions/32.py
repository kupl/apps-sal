n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
x = 0
y = 0
# 価値とコストが0以上である宝石を選ぶ。
for i in range(n):
    if v[i] - c[i] > 0:
        x += v[i]
        y += c[i]
# 選択した宝石の価値とコストの総和差の計算。
print((x - y))
