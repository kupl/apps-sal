def pst(root, curr):
    nonlocal times
    if cs[root - 1] != curr:
        times += 1
    curr = cs[root - 1]
    if root not in vss:
        return
    chn = vss[root]
    for ch in chn:
        pst(ch, curr)


n = int(input())
vs = [int(x) for x in input().split()]

cs = [int(x) for x in input().split()]


# vss = set()
# for i in range(2, n + 1):
#     vss.add((vs[i - 2], i))
#
# vsbp = {v[0]: v for v in vss}
vss = {}
for c, p in enumerate(vs):
    if not p in vss:
        vss[p] = [c + 2]
    else:
        vss[p].append(c + 2)

times = 0


def flattened():
    times = 0
    root = 1
    curr = 0

    firstpart = True

    stack = []
    while True:

        if firstpart:

            if cs[root - 1] != curr:
                times += 1
            curr = cs[root - 1]
            if root not in vss:
                firstpart = False
                if len(stack) == 0:
                    print(times)
                    return
                chni, curr = stack.pop()
            else:
                chn = vss[root]
                chni = iter(chn)

        try:
            ch = next(chni)
            firstpart = True
            root = ch
            stack.append((chni, curr))
        except StopIteration:
            firstpart = False
            if len(stack) == 0:
                print(times)
                return
            chni, curr = stack.pop()

        # if root in vss:
        #     chn = vss[root]
        #     chni = iter(chn)
        #     stack.append((curr, chni))
        # else:
        #     if len(stack) == 0:
        #         print(times)
        #         return


# pst(1, 0)
# print(times)
flattened()
