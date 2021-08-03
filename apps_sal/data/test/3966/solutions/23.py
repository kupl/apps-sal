from sys import stdin


def main():
    stdin.readline()
    l = sorted(list(map(int, stdin.readline().strip().split())))
    tot = delta = sum(l)
    for x in l:
        tot += delta
        delta -= x
    return tot - x


print(main())
