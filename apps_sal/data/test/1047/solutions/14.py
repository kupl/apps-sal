n = int(input())


def nearest(n):
    instr = str(n)
    length = len(instr)
    to_ret = 10**(length - 1)
    for i in range(1, length):
        if int(instr[i]) >= 1:
            to_ret += 10**(length - i - 1)

    return to_ret


i = 0
chisla = []
while n != 0:
    d = nearest(n)
    chisla.append(d)
    n -= d
    i += 1

print(i)
for c in range(i):
    print(chisla[c], end=' ')
