def main():

    five_hundred = int(input())
    one_hundred = int(input())
    fifty = int(input())
    x = int(input())
    ans = 0
    for i in range(five_hundred + 1):
        for j in range(one_hundred + 1):
            for k in range(fifty + 1):
                if 500 * i + 100 * j + 50 * k == x:
                    ans += 1

    print(ans)

def __starting_point():
    main()
__starting_point()
