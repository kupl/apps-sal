count_gift = int(input())
price_list = []
total_payment = 0

for _ in range(count_gift):
    price_list.append(int(input()))

price_list.sort(reverse=True)
total_payment = price_list.pop(0) // 2

for i in price_list:
    total_payment += i

print(total_payment)
