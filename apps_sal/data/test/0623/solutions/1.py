def main():
    (a, b) = map(int, input().split())
    count = 0
    while not (a <= 1 and b <= 1 or a == 0 or b == 0):
        if a < b:
            a += 1
            b -= 2
        else:
            b += 1
            a -= 2
        count += 1
    print(count)


main()
