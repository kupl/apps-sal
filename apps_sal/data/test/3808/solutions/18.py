n = int(input())
s = str(input())


op = 0
cl = 0

b = 0

for c in s:
    if c == '(':
        op += 1
    if c == ')':
        if op > 0:
            op -= 1
        else:
            b += 1


if (b == 1 and op == 1) or (b == 0 and op == 0):
    print('Yes')
else:
    print('No')
