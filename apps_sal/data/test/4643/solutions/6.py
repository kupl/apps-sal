def main():
    try:
        while True:
            for i in range(int(30000000.0)):
                pass
            print(*sorted(map(int, input().split()[1:])))
    except EOFError:
        pass


main()
