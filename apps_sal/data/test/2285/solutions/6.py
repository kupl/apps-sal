def f(s):
    res = []
    sp = s.split(':')
    if not sp[0]:
        sp[0] = '0'
    if not sp[-1]:
        sp[-1] = '0'
    for b in sp:
        if b:
            res.append('{:0>4}'.format(b))
        if not b:
            res.extend(('0000' for i in range(8 - len(sp) + 1)))
    return ':'.join(res)


for i in range(int(input())):
    tmp = input()
    print(f(tmp))
