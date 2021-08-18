

def __starting_point():
    s = input()

    count = 0
    for n in range(3):
        if s[n] == '1':
            count = count + 1

    print(count)


__starting_point()
