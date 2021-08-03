x = int(input())
total = 0
total += (x // 500)
x -= total * 500
total = total * 1000
total += (x // 5) * 5
print(total)
