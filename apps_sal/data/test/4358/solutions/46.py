N = int(input())
sum = 0
price_list = []

for i in range(N):
    price_list.append(int(input()))

ex_product = max(price_list)
dis_ex_product = ex_product // 2

for i in price_list:
    sum += i

answer = sum - dis_ex_product

print(answer)
