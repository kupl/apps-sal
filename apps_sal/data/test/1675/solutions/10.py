__author__ = 'Lipen'


def main():
    n = int(input())
    X = []
    Y = []
    color = [0] * 100001
    for i in range(n):
        (x, y) = map(int, input().split())
        X.append(x)
        Y.append(y)
        color[x] += 1
    s = ''
    for i in range(n):
        z = color[Y[i]]
        s += '{} {}\n'.format(n - 1 + z, n - 1 - z)
    print(s[:-1])


main()
