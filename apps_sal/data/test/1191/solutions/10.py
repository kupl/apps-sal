import operator
class Knight:
    def __init__(self, power, coins, index):
        self.power = power
        self.coins = coins
        self.index = index

class MaxKnight:
    def __init__(self, coins, index):
        self.coins = coins
        self.index = index
nk = input().split(" ")
n = int(nk[0])
k = int(nk[1])

p = input().split(" ")
c = input().split(" ")
for i in range(n):
    p[i] = int(p[i])
    c[i] = int(c[i])
knights = []
for i in range(n):
    kn = Knight(p[i], c[i], i)
    knights.append(kn)
knights.sort(key=operator.attrgetter('power'))

max_c = []
max_knights = []
for i in range(n):
    max_knights.append(sum(max_c) + knights[i].coins)
    if len(max_c) < k:
        max_c.append(knights[i].coins)
    else:
        coins = knights[i].coins
        try:
            if coins > min(max_c):
                max_c.remove(min(max_c))
                max_c.append(coins)
        except:
            pass
# print(max_knights)
for i in range(n):
    max_knights[i] = MaxKnight(max_knights[i], knights[i].index)
max_knights.sort(key=operator.attrgetter('index'))
print(" ".join(str(knight.coins) for knight in max_knights))

