def next(x):
    x = list(x)
    r = -1
    while r >= -len(x) and x[r] == '0':
        r -= 1
    x[r] = chr(ord(x[r]) - 1)
    r -= 1
    while (r > -len(x) - 1 and x[r] == '9'):
        r -= 1
    if (r == -len(x) - 1):
        y = ['1'] + ['0'] * (len(x) - 1) + ['9']
        # print('\t\ty')
        return y
    x[r] = str(int(x[r]) + 1)
    x[len(x) + r + 1:] = ['0'] * (abs(r + 1))
    s = sum([int(z) for z in x])
    x[-1] = str(10 - s + int(x[-1]))
    return x


x = ['1', '9']
k = int(input())
for i in range(k - 1):
    x = next(x)
    #print('\t\t', x)
print(''.join(x))
