import sys
read = sys.stdin.read
readline = sys.stdin.readline
'\na = "dream"[::-1]\nb = "dreamer"[::-1]\nc = "erase"[::-1]\nd = "eraser"[::-1]\n'
s = [*input()]
a = [*'dream']
b = [*'dreamer']
c = [*'erase']
d = [*'eraser']
while True:
    if not s:
        print('YES')
        break
    elif s[-5:] == a:
        for _ in range(5):
            s.pop()
    elif s[-5:] == c:
        for _ in range(5):
            s.pop()
    elif s[-7:] == b:
        for _ in range(7):
            s.pop()
    elif s[-6:] == d:
        for _ in range(6):
            s.pop()
    else:
        print('NO')
        break
