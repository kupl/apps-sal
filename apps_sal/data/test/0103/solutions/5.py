
def main():
    buf = input()
    n = int(buf)
    buf = input()
    buflist = buf.split()
    a = list(map(int, buflist))
    a.insert(0, 0)
    a.append(1001)
    count = -1
    max_count = 0
    last_number = None
    for i, number in enumerate(a):
        if last_number == None:
            pass
        elif number == last_number + 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = -1
        last_number = number
    print(max_count)


def __starting_point():
    main()


__starting_point()
