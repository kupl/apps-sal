s = input().split(" ")
goods_count = int(s[0])
goods = input().split(" ")
t = 0
for i in range(goods_count):
    s = input().split(" ")
    for item in s:
        t += goods.index(item) + 1
        del goods[goods.index(item)]
        goods.insert(0, item)
print(t)
