def meteors(n, ar, br):
    differ = []
    used = {}
    pr = []
    for i in range(n):
        if ar[i] != br[i]:
            pr.append(-1)
            differ.append((i, ar[i], br[i]))
        else:
            pr.append(ar[i])
            used[ar[i]] = i

    unused = find_unused(n, used)

    if len(differ) == 1:
        pr[differ[0][0]] = unused[0]
    elif len(differ) == 2:
        if differ[0][1] in unused and differ[0][2] in unused and differ[1][1] in unused and differ[1][2] in unused: #whatever is fine
            pr[differ[0][0]] = unused[0]
            pr[differ[1][0]] = unused[1]
        if differ[1][1] in unused and differ[1][2] in unused:
            if not differ[0][1] in unused:
                pr[differ[0][0]] = differ[0][2]
                unused.remove(differ[0][2])
                pr[differ[1][0]] = unused[0]
            else:
                pr[differ[0][0]] = differ[0][1]
                unused.remove(differ[0][1])
                pr[differ[1][0]] = unused[0]
        else:
            if not differ[1][1] in unused:
                pr[differ[1][0]] = differ[1][2]
                unused.remove(differ[1][2])
                pr[differ[0][0]] = unused[0]
            else:
                pr[differ[1][0]] = differ[1][1]
                unused.remove(differ[1][1])
                pr[differ[0][0]] = unused[0]
    else:
        pr = list(range(1, n + 1)) # bad input

    return pr

def find_unused(n, used):
    unused = []
    for i in range(1, n + 1):
        if not i in used:
            unused.append(i)
    return unused


def __starting_point():
    n = int(input().strip())
    ar = list(map(int, input().strip().split()))
    br = list(map(int, input().strip().split()))
    print((" ".join(map(str, meteors(n, ar, br)))));

__starting_point()
