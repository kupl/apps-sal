from sys import stdin


def main():
    a = stdin.readline().strip()
    x = a.split('+')
    y = x[1].split('=')
    (d, b, c) = (x[0], y[0], y[1])
    if len(d) + len(b) == len(c):
        print(a)
    elif len(d) + 1 + len(b) == len(c) - 1:
        d = d + '|'
        f = []
        for i in range(len(c)):
            f.append(c[i])
        f.remove(f[i])
        c = ''.join(f)
        e = d + '+' + b + '=' + c
        print(e)
    elif len(d) - 1 + len(b) == len(c) + 1:
        c = c + '|'
        if len(d) > 1:
            f = []
            for i in range(len(d)):
                f.append(d[i])
            f.remove(f[0])
            d = ''.join(f)
        else:
            f = []
            for i in range(len(b)):
                f.append(b[i])
            f.remove(f[0])
            b = ''.join(f)
        e = d + '+' + b + '=' + c
        print(e)
    else:
        print('Impossible')


main()
