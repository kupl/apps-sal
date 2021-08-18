def run():
    n, k = [int(x) for x in input().split()]

    s = input()
    cs = sorted(set(s))
    kcs = {c: i for i, c in enumerate(cs)}

    if k > len(s):
        print(s + (cs[0] * (k - len(s))))
        return

    s = s[:k]
    nr = [kcs[x] for x in s]

    ptr = k - 1
    while True:
        if nr[ptr] < len(cs) - 1:
            nr[ptr] += 1
            break
        nr[ptr] = 0
        ptr -= 1
    print(''.join((cs[x] for x in nr)))


run()
