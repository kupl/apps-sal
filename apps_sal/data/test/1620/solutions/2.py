def __starting_point():
    s = ''
    n = int(input())
    while len(s) < n + 10:
        s += 'aabb'
    print(s[:n])


__starting_point()
