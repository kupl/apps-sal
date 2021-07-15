# B - NarrowRectanglesEasy
def main():
    W, a, b = map(int, input().split())

    if a > b:
        print(max(0, a-b-W))
    else:
        print(max(0, b-a-W))
        
def __starting_point():
    main()
__starting_point()
