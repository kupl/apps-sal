def main():
    s, t = [0] * 123, [0] * 123
    for c in input():
        s[ord(c)] += 1
    for c in input():
        t[ord(c)] += 1
    yay = whoops = 0
    for i, x, y in zip(list(range(123)), s, t):
        if x > y:
            s[i] = x - y
            t[i] = 0
            yay += y
        else:
            s[i] = 0
            t[i] = y - x
            yay += x
    t[ord('A'):ord('Z') + 1], t[ord('a'):ord('z') + 1] = t[ord('a'):ord('z') + 1], t[ord('A'):ord('Z') + 1]
    for i, x, y in zip(list(range(123)), s, t):
        if x > y:
            s[i] = x - y
            t[i] = 0
            whoops += y
        else:
            s[i] = 0
            t[i] = y - x
            whoops += x
    print(yay, whoops)


def __starting_point():
    main()


__starting_point()
