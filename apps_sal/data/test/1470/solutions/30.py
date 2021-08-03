x = int(input())
c = (x + 10) // 11 * 2
if 11 * (c // 2) - 5 >= x:
    c -= 1
print(c)
