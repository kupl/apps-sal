x = int(input())
core = x // 3 * 2
l = x - x // 3 * 3
if l == 0:
    print(core)
else:
    print(core + 1)
