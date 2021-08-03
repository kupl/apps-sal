def main():
    n = int(input())
    b, w = 0, 0
    for x in range(n):
        s = input().split()[1]
        if s == 'soft':
            b += 1
        else:
            w += 1

    for x in range(1, 100):
        a = x ** 2
        a1 = a // 2
        a2 = a - a1

        if max(b, w) <= a2 and min(b, w) <= a1:
            print(x)
            return


main()
