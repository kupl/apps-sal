inpt = [int(i) for i in input().split(' ')]
a = inpt[0]
b = 1
i = 0
while i < inpt[1]:
    ln = [int(j) for j in input().split(' ')]
    ln = sorted(ln)
    if a > ln[1]:
        a = ln[1]
    if b < ln[0]:
        b = ln[0]
    i += 1
if (a - b) >= 0:
    print(a - b)
else:
    print(0)
