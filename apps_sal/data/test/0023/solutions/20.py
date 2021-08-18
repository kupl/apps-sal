def split(integer):
    ret = []
    while integer != 0:
        ret.append(integer % 10)
        integer //= 10
    return ret[::-1]


def combine(lst):
    total = 0
    n = len(lst)
    for i in range(n):
        total += 10 ** (n - i - 1) * lst[i]
    return int(total)


def solve3(a, b):
    al = sorted(list(split(a)))[::-1]
    bl = list(split(b))
    if len(bl) > len(al):
        print(combine(al))
        return

    if a == b:
        print(a)
        return

    ptr = 0
    n = len(al)
    while ptr < n:
        val = bl[ptr]
        selection = al[ptr]
        if selection > val:
            k = al.pop(ptr)
            al.append(k)
        if selection == val:
            if ptr == n - 1:
                print(combine(al))
                break
            else:
                if combine(sorted(al[ptr + 1:])) > combine(bl[ptr + 1:]):
                    k = al.pop(ptr)
                    al.append(k)
                else:
                    ptr += 1
                    al = al[:ptr] + sorted(al[ptr:])[::-1]
        if selection < val:

            print(combine(al[:ptr + 1] + list(sorted(al[ptr + 1:])[::-1])))
            break


a = int(input())
b = int(input())
solve3(a, b)
