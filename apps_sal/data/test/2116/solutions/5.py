(n, m, k) = map(int, input().split())
goods = list(map(int, input().split()))
total_time = 0
for i in range(n):
    goods_i = list(map(int, input().split()))
    for j in range(m):
        pos = goods.index(goods_i[j])
        total_time += pos + 1
        goods.remove(goods_i[j])
        goods = [goods_i[j]] + goods
print(total_time)
