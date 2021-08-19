n = int(input())
product_list = list()
for i in range(1, 10):
    for j in range(1, 10):
        product_list.append(i * j)
if n in product_list:
    print('Yes')
else:
    print('No')
