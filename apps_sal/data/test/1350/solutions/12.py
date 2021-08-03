from collections import Counter
USE_STDIO = False

if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def main():
    n, k = list(map(int, input().split(' ')))
    s = input()
    cnts = Counter(s)
    ans = n
    for i in range(k):
        ch = chr(ord('A') + i)
        ans = min(ans, cnts.get(ch, 0))
    print(ans * k)


def __starting_point():
    main()


__starting_point()
