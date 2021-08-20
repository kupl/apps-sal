inp = input()
inp = inp.split()
gr = 0
n = int(inp[0])
x = int(inp[1])
for i in range(n):
    inp = input()
    inp = inp.split()
    zn = inp[0]
    c = int(inp[1])
    if zn == '+':
        x += c
    elif x - c < 0:
        gr += 1
    else:
        x -= c
print(x, gr)
