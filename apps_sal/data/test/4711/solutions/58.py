(a, b, c) = (int(x) for x in input().split())
gokei1 = a + b
gokei2 = a + c
gokei3 = b + c
resalt = [gokei1, gokei2, gokei3]
print(min(resalt))
