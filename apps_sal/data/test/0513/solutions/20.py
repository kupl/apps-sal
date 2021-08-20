def main(temp):
    nums = []
    for item in temp:
        if item not in nums:
            nums.append(item)
        else:
            return 'ugly'
    Xs = [item[0] for item in nums]
    Ys = [item[1] for item in nums]
    Xset = list(set(Xs))
    Yset = list(set(Ys))
    if len(Xset) != 3 or len(Yset) != 3:
        return 'ugly'
    Xset.sort()
    Yset.sort()
    (a, b, c) = (Xs.count(Xset[0]), Xs.count(Xset[1]), Xs.count(Xset[2]))
    (q, w, e) = (Ys.count(Yset[0]), Ys.count(Yset[1]), Ys.count(Yset[2]))
    if a == c == q == e == 3 and b == w == 2:
        return 'respectable'
    else:
        return 'ugly'


def init():
    nums = []
    for i in range(8):
        nums.append(list(map(int, input().split())))
    print(main(nums))


init()
