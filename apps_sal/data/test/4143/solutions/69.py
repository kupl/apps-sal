def main():
    n = int(input())
    data = [int(input()) for i in range(5)]
    (quo, rem) = divmod(n, min(data))
    print(4 + quo + bool(rem))


main()
