
x = input()
syoku = int(x)

gokei = syoku * 800

if syoku // 15 != 0:
    print(gokei - 200 * (syoku // 15))
else:
    print(gokei)
