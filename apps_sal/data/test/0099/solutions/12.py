a = input().split()
b = int(a[0])
q = int(a[1])
l = int(a[2])
m = int(a[3])
a = input().split()
t = 0
if b == 0:
    if '0' in a:
        print(0)
    else:
        print('inf')
elif abs(b) > l:
    print(0)
elif abs(q) <= 1 and q != -1 and (q != 0):
    if str(b) in a:
        print(0)
    else:
        print('inf')
elif q == -1:
    if str(b) in a and str(-b) in a:
        print(0)
    else:
        print('inf')
elif q == 0:
    t = 1
    if str(b) in a:
        t = 0
    if str(0) in a:
        print(t)
    else:
        print('inf')
else:
    t = 0
    while abs(b) <= l:
        if not str(b) in a:
            t += 1
        b *= q
    print(t)
