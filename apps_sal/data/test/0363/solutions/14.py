n = int(input())
numbers = 0
add = 9
mult = 1
mult2 = 1
while n >= mult2 * 10:
    numbers += 9 * mult * mult2
    mult += 1
    mult2 *= 10
numbers += (n - mult2 + 1) * mult
print(numbers)
