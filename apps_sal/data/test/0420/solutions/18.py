__author__ = 'Lipen'


def main():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(input())

    while n % 2 == 0:
        if a[:n // 2] != a[:n // 2 - 1:-1]:
            break
        n //= 2
        a = a[:n]

    print(n)


main()
