n = int(input())
a = [0] * 200001
mi = 0
ma = 0
input()
for i in range(n - 1):
    r, id = input().split()
    id = int(id)
    if r == 'L':
        mi -= 1
        a[id] = mi
    elif r == 'R':
        ma += 1
        a[id] = ma
    else:
        print(min(a[id] - mi, ma - a[id]))
