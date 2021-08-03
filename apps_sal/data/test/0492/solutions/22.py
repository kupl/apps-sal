a = ['v', '<', '^', '>']
s, e = input().split()
n = int(input())
l = a.index(s)
r = l
n = n % 4
for i in range(n):
    if l == 0:
        l = 3
    else:
        l -= 1
    if r == 3:
        r = 0
    else:
        r += 1
if a[l] == e and a[r] == e:
    print('undefined')
elif a[l] == e:
    print('ccw')
elif a[r] == e:
    print('cw')
