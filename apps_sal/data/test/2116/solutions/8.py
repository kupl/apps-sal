s = input().split()
n = int(s[0])
m = int(s[1])
k = int(s[2])
pos = 0
goods = [int(x) for x in input().split()]
for i in range(n):
    buy = input().split()
    for u in buy:
        x = int(u)
        pos = pos + goods.index(x) + 1
        goods.remove(x)
        goods.insert(0, x)
print(pos)
