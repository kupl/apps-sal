import sys


def main():
    n = int(input())
    tab = sys.stdin.readline()
    s = 1
    t = tab[0]
    e = 0
    for i in range(1, len(tab) - 1):
        if t != tab[i]:
            s += 1
            t = tab[i]
        if tab[i] == tab[i - 1] == '0' or tab[i] == tab[i - 1] == '1':
            e += 1
            e = min(e, 2)
    print(s + e)


main()
