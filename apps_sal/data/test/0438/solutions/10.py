
def main():
    try:
        while True:
            t = n = int(input())
            result = 0
            i = 1
            while n >= i:
                n -= i
                i += 1
                result += 1
            print(result)
            for i in range(1, result):
                print(i, end=' ')
            print(t - sum(range(result)))

    except EOFError:
        pass


main()
