import math


def main():
    a, b = input().split(" ")
    x = math.sqrt(int(a + b))

    print(("Yes" if x.is_integer() else "No"))


main()
