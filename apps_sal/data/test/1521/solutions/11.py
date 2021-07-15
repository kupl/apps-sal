__author__ = 'Adela'


def main():
    p, n = (int(k) for k in input().split())
    full = [False] * p
    for i in range(n):
        xi = int(input())
        mod = xi % p
        if full[mod]:
            print(i+1)
            return
        full[mod] = True

    print(-1)

def __starting_point():
    main()

__starting_point()
