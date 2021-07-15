# C
N = int(input())
# A = list(map(int, input().split()))
order_number = {}


for num, order in enumerate(map(int, input().split())):
    order_number[num+1] = order

for order, number in sorted(order_number.items(), key=lambda x: x[1]):
    print(order, end=" ")
print()
