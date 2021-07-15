def main():
    point = 0
    ab = []
    for i in range(int(input())):
        t = list(map(int, input().split()))
        ab.append(t)
    ab.sort(key=lambda x: x[1])
    for i in range(len(ab)):
        point += ab[i][0]
        # print(point, ab[i])
        if point > ab[i][1]:
            print("No")
            return
    print("Yes")


def __starting_point():
    main()

__starting_point()
