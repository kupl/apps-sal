n, m = map(int, input().split())
li = []
# mの約数を求める
for i in range(int(m**0.5) + 1, 0, -1):
    if i == int(m**0.5) + 1 and (i - 1)**2 == m:
        continue
    if m % i == 0:
        li.append(i)
        li.append(m // i)
li.sort(reverse=True)
# 大きい順に公約数を見ていって条件を満たせばOK
for i in li:
    if n <= m // i:
        print(i)
        break
