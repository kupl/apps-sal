N = int(input())
p = [int(input()) for i in range(N)]

descending_p = sorted(p, reverse=True)

discount_price = descending_p[0] // 2

list_price = sum(descending_p[1:])

total_price = discount_price + list_price
print(total_price)
