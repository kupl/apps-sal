n, q = (int(i) for i in input().split(' '))

oper = {}
for i in range(q):
    key, value = (i for i in input().split(' '))
    oper[key] = value


abc = ['a', 'b', 'c', 'd', 'e', 'f']

all_v = 0
n -= 2


def generate(mystr, num):
    nonlocal all_v
    #print('mystr="%s", num=%d'%(mystr, num))
    try:
        mystr = oper[mystr]
    except KeyError:
        return

    if num == 0:
        if mystr == 'a':
            all_v += 1
        return

    for a in abc:
        generate(mystr + a, num - 1)


for key in oper.keys():
    generate(key, n)

print(all_v)
