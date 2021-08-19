import sys


def main():
    (n, k) = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    b.sort(reverse=True)
    j = 0
    for i in range(n):
        if a[i] == 0:
            a[i] = b[j]
            j += 1
    p = a[0]
    for i in range(1, n):
        if a[i] <= p:
            print('Yes')
            return
        p = a[i]
    print('No')


main()
