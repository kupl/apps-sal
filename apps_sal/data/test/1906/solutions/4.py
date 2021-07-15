def main():
    n = int(input())
    one = n // 2 + n // 3 + n // 5 + n // 7
    two = n // (2*3) + n // (2*5) + n // (2*7) + n // (3*5) + n // (3*7) + n // (5*7)
    three = n // (2*3*5) + n // (2*3*7) + n // (2*5*7) + n // (3*5*7)
    four = n // (2*3*5*7)
    print(n - one + two - three + four)

def __starting_point():
    main()
__starting_point()
