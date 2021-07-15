def main():
    n = int(input())
    words = [input() for _ in range(n)]
    before = words[0][0]
    for w in words:
        if words.count(w) >= 2 or before[-1] != w[0]:
            print('No')
            return
        before = w
    print('Yes')


def __starting_point():
    main()
__starting_point()
