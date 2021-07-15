x = int(input())

div, mod = divmod(x, 11)

add = 0
if 0 < mod <= 6:
    add = 1
elif mod > 6:
    add = 2

print(div * 2 + add)
