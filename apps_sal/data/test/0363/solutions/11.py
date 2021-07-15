__author__ = 'KostikBigOne'

def main():
    n = int(input())
    power, cnt = 1, 9
    ans = 0
    length = 1
    while True:
        if n >= 10 * power:
            ans += length * cnt
            cnt *= 10
            power *= 10
            length += 1
        else:
            ans += length * (n - power + 1)
            break
    print(ans)

def __starting_point():
    main()
__starting_point()
