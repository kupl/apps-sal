from collections import defaultdict
import sys
read = sys.stdin.read


def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    rems = defaultdict(int)
    n = 7 % k
    next_digit = 70 % k
    r = 1
    while True:
        if n == 0:
            print(r)
            return
        elif rems[n]:
            print(-1)
            return
        else:
            rems[n] = 1
            n += next_digit
            n = n % k
            next_digit = next_digit * 10 % k
            r += 1


def __starting_point():
    main()


__starting_point()
