import sys

r, c = [int(x) for x in sys.stdin.readline().split()]

for i in range(1, r + 1):
    if i % 2 == 1: print("#" * c)
    else:
        if i % 4 == 2: print("." * (c - 1) + "#")
        else: print("#" + "." * (c - 1))
