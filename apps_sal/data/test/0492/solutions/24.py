(a, b) = input().split()
n = int(input())
d = {'^': 0, '>': 1, 'v': 2, '<': 3}
e = {'^': 0, '>': 3, 'v': 2, '<': 1}
f1 = f2 = 0
if (d[a] + n) % 4 == d[b]:
    f1 = 1
if (e[a] + n) % 4 == e[b]:
    f2 = 1
if f1 and f2:
    print('undefined')
else:
    print('cw' if f1 else 'ccw')
