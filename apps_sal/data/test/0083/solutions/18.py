n = int(input())
a = [int(s) for s in input().split()]
pol = 0
neg = 0
nul = 0

for el in a:
    if el > 0:
        pol += 1
    elif el < 0:
        neg += 1
    else:
        nul += 1

polov = n // 2 + n % 2
d = 0
if pol >= polov:
    d = 1
elif neg >= polov:
    d = -1
print(d)
