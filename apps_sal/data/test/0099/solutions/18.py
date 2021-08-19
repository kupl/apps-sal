(b, q, l, m) = [int(a_temp) for a_temp in input().strip().split()]
a = [int(a_temp) for a_temp in input().strip().split()]
d = {}
for e in a:
    d[e] = True
if abs(b) > l:
    print(0)
elif q == 0:
    if 0 not in d:
        print('inf')
    elif b not in d:
        print(1)
    else:
        print(0)
elif b == 0:
    if 0 not in d:
        print('inf')
    else:
        print(0)
elif q == 1:
    if b in d or abs(b) > l:
        print(0)
    else:
        print('inf')
elif q == -1:
    if abs(b) > l:
        print(0)
    elif b not in d:
        print('inf')
    elif -1 * b not in d:
        print('inf')
    else:
        print(0)
else:
    count = 0
    t = b
    while abs(t) <= l:
        if t not in d:
            count += 1
        t *= q
    print(count)
