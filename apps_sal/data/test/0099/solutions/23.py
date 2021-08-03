b, q, l, m = [int(x) for x in input().split()]
seq = [int(x) for x in input().split()]

wyn = 0
while abs(b) <= l:
    if b == 0 or q == 0:
        if 0 not in seq:
            print("inf")
        elif b != 0 and b not in seq:
            print(1)
        elif b == 0 or b != 0 and b in seq:
            print(0)
        return

    if q == 1:
        if b in seq:
            print(0)
        else:
            print("inf")
        return

    if q == -1:
        if b in seq and b * -1 in seq:
            print(0)
        else:
            print("inf")
        return

    if b not in seq:
        wyn += 1
    b *= q
print(wyn)
