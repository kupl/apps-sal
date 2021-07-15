a = input()
if len(a) == 2:
    print(0)
else:
    a = a.split(', ')
    a[0] = a[0][1:]
    a[-1] = a[-1][:1]
    print(len(set(a)))
