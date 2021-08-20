z = input
'\n\nn=int(z())\n\nfor i in range(n):\n\nx=int(z())\n\nl=list(map(int,z().split()))\n\na,b=map(int,z().split())\n\nx=z()\n\n'
n = int(z())
for i in range(n):
    x = z()
    one = x.count('1')
    ze = x.count('0')
    p = min(one, ze)
    if p % 2 != 0:
        print('DA')
    else:
        print('NET')
