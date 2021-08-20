from sys import stdin as cin


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = input()
    (l, r) = ('?', '?')
    for i in range(1, n):
        if b[i] == '1' and b[i - 1] == '0':
            if l == '?':
                l = 1 + max(a[i], a[i - 1], a[i - 2], a[i - 3], a[i - 4])
            else:
                l = max(l, 1 + max(a[i], a[i - 1], a[i - 2], a[i - 3], a[i - 4]))
        if b[i] == '0' and b[i - 1] == '1':
            if r == '?':
                r = min(a[i], a[i - 1], a[i - 2], a[i - 3], a[i - 4]) - 1
            else:
                r = min(r, min(a[i], a[i - 1], a[i - 2], a[i - 3], a[i - 4]) - 1)
    if l == '?':
        l = -1000000000
    if r == '?':
        r = 1000000000
    print(l, r)


main()
