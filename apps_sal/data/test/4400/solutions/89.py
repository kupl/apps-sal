s = input()

if s == 'SSS':
    print(0)

if s == 'SSR' or s == 'SRS' or s == 'RSS' or s == 'RSR':
    print(1)

if s == 'SRR' or s == 'RRS':
    print(2)

if s == 'RRR':
    print(3)
