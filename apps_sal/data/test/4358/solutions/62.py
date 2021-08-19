N = int(input())
p = [int(input()) for i in range(N)]

descending_p = sorted(p, reverse=True)
# print(descending_p)

# 一番の高額は半額
discount_price = descending_p[0] // 2
# print(discount_price)

# 他は定価で買う
list_price = sum(descending_p[1:])
# print(list_price)

total_price = discount_price + list_price
print(total_price)
