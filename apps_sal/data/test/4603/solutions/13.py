# 電車　通常切符A円、乗り放題B円
# バス　通常切符C円、乗り放題D円
a = int(input())
b = int(input())
c = int(input())
d = int(input())

total_fare = (min(a, b) + min(c, d))

print(total_fare)
