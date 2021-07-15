def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = [0] * 5
    balance = [0] * 5

    for e in a:
        count[e - 1] += 1
        balance[e - 1] += 1
    for e in b:
        count[e - 1] += 1
        balance[e - 1] -= 1

    for e in count:
        if e % 2 != 0:
            print(-1)
            return
    print(sum([abs(i) for i in balance]) // 4)


def __starting_point():
    main()
__starting_point()
