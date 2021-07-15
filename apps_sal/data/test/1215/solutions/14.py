
def main():
    buf = input()
    n = int(buf)
    if n % 2 == 1:
        print(0) # impossible
    else:
        print(int(2 ** (n // 2)))

def __starting_point():
    main()

__starting_point()
