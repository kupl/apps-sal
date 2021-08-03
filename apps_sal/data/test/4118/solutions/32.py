a, b = map(int, input().split())


def mult(a, b):
    if a > 9 or b > 9 or a < 1 or b < 1:
        print(-1)
    else:
        print(a * b)


mult(a, b)
