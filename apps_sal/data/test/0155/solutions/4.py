# python3

def readline(): return tuple(map(int, input().split()))


def main():
    n, m, k = readline()
    if k < n:
        print(k + 1, 1)
    else:
        k -= n
        q, r = divmod(k, m - 1)
        print(n - q, m - r if q & 1 else 2 + r)


main()
