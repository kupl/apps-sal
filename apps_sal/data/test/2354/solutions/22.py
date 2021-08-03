import sys
f = sys.stdin


def answer1(x, y):
    a = 1
    val = round((n**2) / 2)
    if (x + y) & 1 == 1:
        a += val
    x1 = a + (x - 1) * (n // 2)
    y1 = x1 + (((y + 1) // 2) - 1)
    sys.stdout.write(str(y1) + '\n')


def answer2(x, y):
    a = 1
    val = (n**2) // 2
    if n & 1 == 1:
        val += 1
    if (x + y) & 1 == 1:
        a += val
        # print(val)
    x1 = a + (((x + 1) // 2) - 1) * n
    if x & 1 == 0:
        y += n
    y1 = x1 + (((y + 1) // 2) - 1)
    sys.stdout.write(str(y1) + '\n')


def find(x, y):
    if n & 1 == 0:
        answer1(x, y)
    else:
        answer2(x, y)


n, q = map(int, f.readline().rstrip('\r\n').split())
for _ in range(q):
    x, y = map(int, f.readline().rstrip('\r\n').split())
    find(x, y)
