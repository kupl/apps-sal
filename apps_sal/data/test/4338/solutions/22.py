from math import ceil


def mi():
    return list(map(int, input().split()))


'''
6 3 2
2 3 1 3 4 2
'''
n, x, y = mi()
a = list(mi())

le = 0
for i in a:
    if i <= x:
        le += 1
if y >= x:
    print(ceil(le / 2))
else:
    print(n)
