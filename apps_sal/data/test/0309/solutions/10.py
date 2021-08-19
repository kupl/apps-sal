def maximum(l, r):

    r = bin(r)[2:]
    l = bin(l)[2:].zfill(len(r))

    if r[0] == "1" and l[0] == "0":
        return int("1" * len(l), base=2)
    else:
        # print(l,r)

        if l[1:] != "":

            l = int(l[1:], base=2)
            r = int(r[1:], base=2)

        else:
            return 0

        return maximum(l, r)


inp = input()
l, r = inp.split(" ")
print(maximum(int(l), int(r)))
