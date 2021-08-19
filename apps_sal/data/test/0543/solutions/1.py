def main():
    try:
        while True:
            n = int(input())
            rem = False
            for x in map(int, input().split()):
                if x & 1:
                    rem = not rem
                elif rem and x == 0:
                    print('NO')
                    break
            else:
                print('NO' if rem else 'YES')
    except EOFError:
        pass


main()
