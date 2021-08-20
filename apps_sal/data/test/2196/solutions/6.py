from sys import stdin, stdout
n = int(stdin.readline())
y = s = x = 0
for i in map(int, stdin.readline().split()):
    if i == y:
        x += 1
    else:
        while x and i > y:
            if not x & 1:
                s += 1
            x >>= 1
            y += 1
        if i > y:
            s += i - y
            (x, y) = (1, i)
        else:
            x += 1
while x:
    if not x & 1:
        s += 1
    x >>= 1
print(s)
