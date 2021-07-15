def B():
    n = int(input())
    lst = list(input())

    for i in range(len(lst)):
        if lst[i] == "r":
            lst[i] = 1
        else:
            lst[i] = -1

    rCo = 0
    bCo = 0
    co = 0
    cur = lst[0]

    if n == 1:
        print("0")
        return 0

    for i in range(len(lst)):
        if lst[i] == cur:
            cur *= -1
            continue
        else:
            if lst[i] == 1:
                if bCo != 0:
                    bCo -= 1
                else:
                    rCo += 1
                    co += 1
            else:
                if rCo != 0:
                    rCo -= 1
                else:
                    bCo += 1
                    co += 1
            cur *= -1

    first = co

    rCo = 0
    bCo = 0
    co = 0
    cur = lst[0] * -1
    for i in range(len(lst)):
        if lst[i] == cur:
            cur *= -1
            continue
        else:
            if lst[i] == 1:
                if bCo != 0:
                    bCo -= 1
                else:
                    rCo += 1
                    co += 1
            else:
                if rCo != 0:
                    rCo -= 1
                else:
                    bCo += 1
                    co += 1
            cur *= -1

    print(min(co, first))
    return 0

def __starting_point():
    B()
__starting_point()
