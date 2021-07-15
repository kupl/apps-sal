def print_all():
    print(top)
    print(free_top)
    print(busy_top)
    print(bottom)
    print(free_bottom)
    print(busy_bottom)

n = int(input())
top = set()
bottom = set()
for i in range(n):
    name, type = input().split()
    if type == '1':
        top.add(name)
    else:
        bottom.add(name)

top_order = set(str(i) for i in range(1, len(top) + 1))
bottom_order = set(str(i) for i in range(len(top) + 1, len(bottom) + len(top) + 1))
q = top_order & top
top_order -= q
top -= q
q = bottom_order & bottom
bottom_order -= q
bottom -= q

busy_top = top_order & bottom
free_top = top_order - bottom
busy_bottom = bottom_order & top
free_bottom = bottom_order - top

if len(top_order) + len(bottom_order) == 0:
    print(0)
    return

if len(free_bottom) + len(free_top) == 0:
    x, y = busy_top.pop(), 'rft330'
    free_top.add(x)
    bottom.remove(x)
    bottom.add(y)
    print(len(top_order) + len(bottom_order) + 1)
    print('move', x, y)
else:
    print(len(top_order) + len(bottom_order))

cross_block = min(len(busy_bottom), len(busy_top))
if len(free_top) > 0 and cross_block > 0:
    x = free_top.pop()
    for i in range(cross_block):
        x, y = busy_bottom.pop(), x
        top.remove(x)
        print('move', x, y)
        x, y = busy_top.pop(), x
        bottom.remove(x)
        print('move', x, y)
    free_top.add(x)

cross_block = min(len(busy_bottom), len(busy_top))
if len(free_bottom) > 0 and cross_block > 0:
    x = free_bottom.pop()
    for i in range(cross_block):
        x, y = busy_top.pop(), x
        bottom.remove(x)
        print('move', x, y)
        x, y = busy_bottom.pop(), x
        top.remove(x)
        print('move', x, y)
    free_bottom.add(x)

if len(busy_bottom) == 0:
    for i in range(len(bottom)):
        print('move', bottom.pop(), free_bottom.pop())
    free_top |= busy_top
    busy_top.clear()
    for i in range(len(top)):
        print('move', top.pop(), free_top.pop())
elif len(busy_top) == 0:
    for i in range(len(top)):
        print('move', top.pop(), free_top.pop())
    free_bottom |= busy_bottom
    busy_bottom.clear()
    for i in range(len(bottom)):
        print('move', bottom.pop(), free_bottom.pop())

