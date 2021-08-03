from sys import stdin


def main():
    n, l = list(map(int, stdin.readline().strip().split()))
    aa = sorted(map(int, stdin.readline().strip().split()))
    maxgap = max(aa[0], l - aa[-1]) * 2
    a = aa[0]
    for b in aa:
        gap, a = b - a, b
        if maxgap < gap:
            maxgap = gap
    return maxgap / 2


print(main())
