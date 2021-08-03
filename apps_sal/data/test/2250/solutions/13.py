def calc_one(n):
    frac = n / 3
    if frac % 1 == 0:
        return int(frac)
    return int(frac + 1)  # ceil


def calc_ops(L):
    frac = (L - 2) / 3
    if frac % 1 == 0:
        return int(frac)
    return int(frac + 1)    # ceil


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        l = []
        c = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                c += 1
            else:
                l.append(c)
                c = 1
        if s[0] == s[-1]:
            if len(l) == 0:
                l.append(c)
            else:
                l[0] += c
        else:
            l.append(c)
        if len(l) == 1:
            print(calc_one(n))
        else:
            total = 0
            for j in l:
                total += calc_ops(j)
            print(total)


main()
