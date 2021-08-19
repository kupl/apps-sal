def resolve():
    from math import ceil
    X = int(input())
    print(X // 11 * 2 + ceil(X % 11 / 6))


resolve()
