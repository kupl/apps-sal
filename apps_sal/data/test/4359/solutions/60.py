x = list(map(int, (input() for i in range(5))))
y = sorted(x, key=lambda x: ((x + 9) // 10) * 10 - x)

s = 0
for z in y[:-1]:
    s += ((10 + z - 1) // 10) * 10
print((s + y[-1]))
