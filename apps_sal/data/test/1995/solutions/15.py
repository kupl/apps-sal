def main():
    mode = "filee"
    if mode == "file":
        f = open("test.txt", "r")

    def get(): return [int(x) for x in (f.readline() if mode == "file" else input()).split()]
    s = list(input())
    [m] = get()
    for z in range(m):
        [l, r, k] = get()
        l -= 1
        if k > r - l:
            k = k % (r - l)
        temp = s[:l] + s[r - k:r] + s[l:r - k] + s[r:]
        s = temp
    print("".join(s))

    if mode == "file":
        f.close()


def __starting_point():
    main()


__starting_point()
