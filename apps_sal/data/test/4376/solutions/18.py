def main():
    (n, m) = list(map(int, input().split()))
    room = [int(x) for x in input().split()]
    letter = [int(x) for x in input().split()]
    room_num = 0
    j = 0
    for d in range(n):
        while j < m and letter[j] <= room_num + room[d]:
            r = letter[j] - room_num
            print(d + 1, r)
            j += 1
        room_num += room[d]


def __starting_point():
    main()


__starting_point()
