def ss(a):
    if a > 9:
        return str(a)
    else:
        return '0' + str(a)


a = [int(x) for x in input().split(':')]
b = [int(x) for x in input().split(':')]
h = a[0] - b[0]
m = a[1] - b[1]
hh = 0
while m < 0:
    m = 60 - abs(m)
    hh += 1
h -= hh
while h < 0:
    h = 24 - abs(h)
print(ss(h), ':', ss(m), sep='')
