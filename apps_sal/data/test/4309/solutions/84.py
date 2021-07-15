def main():
    n = int(input())
    for i in range(n, 1000):
        if len(set(list(str(i)))) == 1:
            print(i)
            return


main()

