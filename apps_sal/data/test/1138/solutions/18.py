import collections


def main():
    s = input()
    if len(s) % 2 == 1:
        print(-1)
        return
    ct = collections.Counter(s)
    print((abs(ct['L'] - ct['R']) + abs(ct['U'] - ct['D'])) // 2)


main()
