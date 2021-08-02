P = print
I = input
I()
a = b = 0
t = []
for x in map(int, I().split()):
    if x < 0:
        if b == 2:
            t += [a]
            b = 1
            a = 0
        else:
            b += 1
    a += 1
if a:
    t += [a]
P(len(t))
for x in t:
    P(x, end=' ')
