from sys import stdin


def main():
    n = int(stdin.readline())
    l = list(map(int, stdin.readline().split()))
    while True:
        l.sort()
        i = max(list(range(1, n)), key=lambda _: l[_] - l[_ - 1])
        if l[i] == l[i - 1]:
            return sum(l)
        l[i] -= l[i - 1]


print(main())
