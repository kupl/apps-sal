
def main():
    n = int(input())
    items = input().split(" ")
    s = 0
    for p in items:
        s += int(p) + 1
        print(2 - (s & 1))



def __starting_point():
    main()
__starting_point()
