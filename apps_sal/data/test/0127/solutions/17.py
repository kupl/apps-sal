n, f = list(map(int, input().split()))

products_and_clients_per_day = []

for i in range(n):
    k, l = list(map(int, input().split()))
    normal_sales = min(k, l)
    double_sales = min(2 * k, l)
    sell_out_profit = double_sales - normal_sales
    products_and_clients_per_day.append((k, l, sell_out_profit))


products_and_clients_per_day.sort(key=lambda x: x[2], reverse=True)

res = 0

for i in range(f):
    k, l, sell_out_profit = products_and_clients_per_day[i]
    double_sales = min(2 * k, l)
    res += double_sales

for i in range(f, n):
    k, l, sell_out_profit = products_and_clients_per_day[i]
    normal_sales = min(k, l)
    res += normal_sales

print(res)
