def main():
    input()
    s = input()
    d = dict.fromkeys(s, 0)
    le, res = len(d), []
    iti, itj = (iter(enumerate(s)) for _ in "12")
    try:
        while True:
            while le:
                i, c = next(iti)
                if d[c]:
                    d[c] += 1
                else:
                    d[c] = 1
                    le -= 1
            while True:
                j, c = next(itj)
                if d[c] > 1:
                    d[c] -= 1
                else:
                    d[c], le = 0, 1
                    res.append(i - j)
                    break
    except StopIteration:
        print(min(res) + 1)


def __starting_point():
    main()

__starting_point()
