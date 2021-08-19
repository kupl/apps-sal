import sys


def main():
    n = int(input())
    sushi = list(map(int, sys.stdin.readline().split()))
    (debut, milieu, fin) = (0, 0, 1)
    maxLong = 0
    for i in range(1, n):
        if sushi[i] == sushi[i - 1]:
            fin += 1
        else:
            maxLong = max(maxLong, 2 * min((fin - milieu, milieu - debut)))
            debut = milieu
            milieu = fin
            fin += 1
    maxLong = max(maxLong, 2 * min((n - milieu, milieu - debut)))
    print(maxLong)


main()
