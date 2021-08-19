def main():
    try:
        while True:
            n = int(input())
            x = 1
            a = 1378
            while n != 0:
                if n & 1:
                    x *= a
                    x %= 10000
                a *= a
                a %= 10000
                n >>= 1
            print(x % 10)
    except EOFError:
        pass


main()
