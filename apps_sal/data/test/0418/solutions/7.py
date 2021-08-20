3


def main():
    n = int(input())
    ans = False
    for i in range(n):
        (name, old, new) = input().split()
        old = int(old)
        new = int(new)
        if new > old and old >= 2400:
            ans = True
    print('YES' if ans else 'NO')


main()
