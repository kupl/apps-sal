s = input()
if s == 'SSS':
    print((0))
elif s == 'RRR':
    print((3))
elif s == 'SRR' or s == 'RRS':
    print((2))
elif s == 'SSR' or s == 'RSR' or s == 'SRS' or s == 'RSS':
    print((1))
