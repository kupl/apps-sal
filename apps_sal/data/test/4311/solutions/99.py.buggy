from sys import stdin

s = int(stdin.readline().strip())
mem = []
a = s

for i in range(1000000):
    if a in mem:
        print(i + 1)
        return
    mem.append(a)
    if a % 2 == 0:
        a = a // 2
    else:
        a = 3 * a + 1
