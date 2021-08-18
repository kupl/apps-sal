import collections
# input
def R(): return map(int, input().split())


x, y = R()

tx = y - 1
if y == 1:
    if x != 0:
        print('No')
        return
    else:
        print('Yes')
        return
if y == 0:
    print('No')
    return
if x >= tx and (x - tx) % 2 == 0:
    print('Yes')
    return
print('No')
