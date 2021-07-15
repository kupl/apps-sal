positions = ">v<^"

s, t = input().split()
n = int(input())

si = positions.index(s)
ti_cw = positions[(si + n) % 4]
ti_ccw = positions[(si - n) % 4]

if n % 2 == 0:
    print('undefined')
elif t == ti_cw:
    print('cw')
elif t == ti_ccw:
    print('ccw')
else:
    assert False
