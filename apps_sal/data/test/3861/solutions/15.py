input()
sqrs = set()
x = 0
while x ** 2 <= 10 ** 6:
    sqrs.add(x ** 2)
    x += 1
print(max([x for x in map(int, input().split()) if x not in sqrs]))
