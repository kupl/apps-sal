import sys
inp = sys.stdin.readline().split()
t = int(inp[0])
s = int(inp[1])
x = int(inp[2])


def fn():
    if x == t:
        return 'YES'
    if x < s + t:
        return 'NO'
    if (x - t) % s <= 1:
        return 'YES'
    return 'NO'


print(fn())
