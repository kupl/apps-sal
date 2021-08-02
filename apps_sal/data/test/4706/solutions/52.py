def main():
    cat = "".join
    data = cat(input() for _ in range(3))
    print((cat([data[0], data[4], data[8]])))


main()
