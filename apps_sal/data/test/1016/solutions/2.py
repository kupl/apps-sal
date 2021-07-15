import itertools

a, b = list(map(int, input().split()))

dang = 1

#w = [x+1 for x in range(a)]
r = [(x, set()) for x in range(a)]

for i in range(b):
     x, y = list(map(int, input().split()))
     x, y = x-1, y-1

     r[x][1].add(y)
     r[y][1].add(x)


r = sorted(r, key=lambda x: len(x[1]), reverse=True)
willreact = r[0][1]
del r[0]

#print('r:', r)
#print('wr:', willreact)

while len(r) > 0:
    dr = 0
    for i in range(len(r)):
        if r[i][0] in willreact:
            willreact |= r[i][1]
            dang *= 2
            del r[i]
            dr = 1
            break
    if dr == 0:
        willreact |= r[0][1]
        del r[0]

print(dang)

