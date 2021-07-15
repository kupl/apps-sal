x = int(input())

thousand = x // 500
rest = x - thousand * 500
five = rest // 5

print((thousand * 1000 + five * 5))

