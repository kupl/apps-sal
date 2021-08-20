a = list(input())
b = []
for i in range(int(len(a))):
    t = a[int(i)]
    if t == '0':
        b.append('0')
    elif t == '1':
        b.append('1')
    elif len(b) > 0:
        del b[-1]
print(''.join(b))
