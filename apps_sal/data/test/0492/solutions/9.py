s, e = input().split()
n = int(input()) % 4
sp = ['v', '<', '^', '>']
i = sp.index(s)
j = i

while n > 0:
    i = (i + 1) % 4
    j = (j - 1) % 4
    n -= 1
if e == sp[i] and e != sp[j]:
    print('cw')
elif e == sp[j] and e != sp[i]:
    print('ccw')
else:
    print('undefined')
