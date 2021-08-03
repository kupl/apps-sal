def main():
    n = int(input())
    data = [int(input()) for i in range(5)]
    quo, rem = divmod(n, min(data))
    quo = 5 + quo
    if rem:
        print(quo)
    else:
        print(quo - 1)


main()
