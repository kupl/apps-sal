num = int(input())
add = 0
if num % 32 < 16:
    if num % 2 == 1:
        add += 15
elif num % 2 == 0:
    add -= 15
if num % 16 < 8:
    if num % 8 >= 4:
        add += 4
elif num % 8 < 4:
    add -= 4
num += add
print(num)
