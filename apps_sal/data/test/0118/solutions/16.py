3


def main():
    (t, s, x) = list(map(int, input().split()))
    if x == t:
        print('YES')
        return
    x -= t + s
    if x >= 0 and x % s == 0 or (x >= 1 and (x - 1) % s == 0):
        print('YES')
    else:
        print('NO')


main()
