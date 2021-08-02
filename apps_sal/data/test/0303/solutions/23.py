def main():
    x1, y1, x2, y2 = list(map(int, input().split()))
    a, b = list(map(int, input().split()))

    xd = x2 - x1
    yd = y2 - y1

    if xd % a != 0 or yd % b != 0:
        print('NO')
        return

    xd /= a
    yd /= b

    print("YES" if (xd % 2) == (yd % 2) else "NO")


main()
