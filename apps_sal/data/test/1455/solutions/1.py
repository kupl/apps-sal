
def main():
    buf = input()
    n = int(buf)
    m = n // 2 + 1
    print(m)
    for i in range(m):
        print(1, i+1)
        n -= 1
    for i in range(m):
        if n > 0:
            print(i+2, m)
            n -= 1

def __starting_point():
    main()

__starting_point()
