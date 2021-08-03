x1, y1, x2, y2, x3, y3 = list(map(int, input().split(' ')))


def main():
    b1 = (x2 - x1) ** 2 + (y2 - y1) ** 2 == (x3 - x2) ** 2 + (y3 - y2) ** 2
    b2 = (y3 - y1) * (x2 - x1) != (y2 - y1) * (x3 - x1)

    return b1 and b2


print('Yes' if main() else 'No')
