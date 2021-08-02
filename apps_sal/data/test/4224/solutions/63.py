def mai():
    input()
    t = list(map(int, input().split()))
    t.sort(reverse=True)
    count = 0
    val = t[0]
    tmp_count = 0
    for v in t:
        while v % 2 == 0:
            v //= 2
            tmp_count += 1
    print(tmp_count)


def __starting_point():
    mai()


__starting_point()
