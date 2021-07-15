s = list(input())
d = int(s[-1])

last_pos = None

for i, x in enumerate(s[:-1]):
    if int(x) % 2 == 0:
        if int(x) < d:
            s[i] = str(d)
            s[-1] = x
            last_pos = None
            print(''.join(s))
            break
        elif int(x) != d:
            last_pos = i
else:
    if last_pos is None:
        print('-1')
    else:
        t = s[last_pos]
        s[last_pos] = s[-1]
        s[-1] = t
        print(''.join(s))
