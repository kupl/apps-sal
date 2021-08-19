def main():
    N = int(input())
    (x, y) = list(map(int, input().split()))
    a1 = x + y
    a2 = x + y
    b1 = y - x
    b2 = y - x
    N -= 1
    while N != 0:
        (x, y) = list(map(int, input().split()))
        a1 = max(a1, x + y)
        a2 = min(a2, x + y)
        b1 = max(b1, y - x)
        b2 = min(b2, y - x)
        N = N - 1
    print(max(a1 - a2, b1 - b2))


main()
