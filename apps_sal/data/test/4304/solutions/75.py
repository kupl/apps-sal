import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
a, b = [int(num) for num in lines.pop(0).split(" ")]
dif = b - a
height = dif * (dif - 1)  // 2
print((height - a))

