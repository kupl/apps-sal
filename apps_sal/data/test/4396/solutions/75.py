import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    m = [tuple(input().split()) for _ in range(n)]
    btc_to_jpy = 380000
    ans = 0
    for price, kind in m:
        if kind == 'JPY':
            ans += int(price)
        else:
            ans += btc_to_jpy * float(price)
    print(ans)


def __starting_point():
    main()


__starting_point()
