def main():
    n = int(input())
    nulls = fives = 0
    for item in input().split():
        if int(item) == 0:
            nulls += 1
        else:
            fives += 1
    if nulls >= 1:
        if fives >= 9:
            print(int('5' * (fives - fives % 9) + '0' * nulls))
        else:
            print(0)
    else:
        print(-1)


main()
