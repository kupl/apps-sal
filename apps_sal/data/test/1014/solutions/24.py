def main():
    n = int(input()) & 1
    print(('white', 'black')[n])
    if not n:
        print(1, 2)


main()

