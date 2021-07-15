l, r = ['{:061b}'.format(int(x)) for x in input().split()]

pot = 0
for i in range(61):
    if l[i] != r[i]:
        pot = 61 - i
        break

if pot == 0:
    print(0)
else:
    print((2**pot - 2) ^ 1)
