__author__ = 'Lipen'


def main():
    (n, s) = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) - max(a) <= s:
        print('YES')
    else:
        print('NO')


main()
