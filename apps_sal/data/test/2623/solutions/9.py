T = int(input())
for case in range(T):
    n, k = [int(x) for x in input().split()]
    s = input()
    ls = sorted(list(s))
    # print(ls)
    ret = ""
    # while len(ls) != 0:
    alset = set(ls[:k])
    # for i in range(k):
    # alset.add(ls[i])
    #ret[i] += ls[i]
    if len(alset) == 1:
        ret += ls[0]
        if len(set(ls[k:])) == 1:
            ret += str(ls[k]) * ((len(ls[k:]) - 1) // k + 1)
        else:
            ret += "".join(ls[k:])
    else:
        ret += ls[k - 1]
        # break

    print(ret)
