def input_split(f):
    return list(map(f, input().split()))


def main():
    (x1, y1) = input_split(int)
    (x2, y2) = input_split(int)
    n = int(input())
    count = 0
    for i in range(n):
        (a, b, c) = input_split(int)
        if (a * x1 + b * y1 + c) * (a * x2 + b * y2 + c) < 0:
            count += 1
    print(count)


main()
