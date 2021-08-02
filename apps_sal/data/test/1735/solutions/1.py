res = 1
stack = ['1', '2']
for c in input():
    sp = stack.pop()
    if c != sp:
        stack.append(sp)
        stack.append(c)
    else:
        res = 3 - res
if res != 1:
    print('Yes')
else:
    print('No')
