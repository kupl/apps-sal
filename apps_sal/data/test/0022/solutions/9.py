a = 'AHIMOTUVWXYovwx'
b = 'bdpq'
c = 'dbqp'
l = list(zip(a, a)) + list(zip(b, c))
s = input()


def f(c):
    for x in l:
        if c == x[0]:
            return x[1]
    return ' '


t = ''.join(map(f, s[::-1]))
print('TAK' if s == t else 'NIE')
