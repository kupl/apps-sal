bus_a = int(input())
bus_b = int(input())
train_a = int(input())
train_b = int(input())
fee_list = [bus_a + train_a, bus_a + train_b, bus_b + train_a, bus_b + train_b]
fee_list.sort()
print(fee_list[0])
