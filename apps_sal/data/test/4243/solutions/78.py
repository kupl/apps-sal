x = int(input())
c1 = x // 500
x -= 500 * c1
c2 = x // 5
print(1000 * c1 + 5 * c2)
