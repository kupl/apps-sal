import sys
n, x = [int(x) for x in sys.stdin.readline().split()]
bad = 0
for i in range(n):
    sym, num = sys.stdin.readline().split()
    if sym == "+":
        x += int(num)
    else:
        if x < int(num):
            bad += 1
        else:
            x -= int(num)
print(x, bad)

