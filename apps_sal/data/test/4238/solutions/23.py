# coding: utf-8
# Your code here!
def main():
    num = sum(list(map(lambda x: int(x), input())))
    if num % 9 == 0:
        print("Yes")
    else:
        print("No")


def __starting_point():
    main()


__starting_point()
