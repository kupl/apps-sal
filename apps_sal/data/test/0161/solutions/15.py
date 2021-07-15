x = int(input())


op = 0
ans = []
while '0' in (bin(x)[2:]):
    if op % 2 == 0:
        can = int('1' * (len(bin(x)[2:]) - bin(x)[2:].index('0')), 2)
        x ^= can
        ans += [len(bin(can)) - 2]
    else:
        x += 1
    op += 1

print(op)
for a in ans:
    print(a, end= ' ')
