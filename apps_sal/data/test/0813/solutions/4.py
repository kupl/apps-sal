__author__ = 'Lipen'


def main():
    n, a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    s = ''
    for i in range(1, n + 1):
        if i in A:
            s += '1 '
        else:
            s += '2 '

    print(s[:-1])


main()
