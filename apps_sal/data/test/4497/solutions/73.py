def main():
    n = int(input())

    if 64 <= n <= 100:
        print(64)
    elif 32 <= n <= 63:
        print(32)
    elif 16 <= n <= 31:
        print(16)
    elif 8 <= n <= 15:
        print(8)
    elif 4 <= n <= 7:
        print(4)
    elif 2 <= n <= 3:
        print(2)
    else:
        print(1)


if __name__ == "__main__":
    main()
