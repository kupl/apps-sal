def main():
    x, y = map(int, input().split())
    if abs(x-y) <= 1:
        print("Brown")
    else:
        print("Alice")

def __starting_point():
    main()
__starting_point()
