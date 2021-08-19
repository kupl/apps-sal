from itertools import product


def p_factorization_t(n):
    if n == 1:
        return []
    pf_cnt = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            pf_cnt.append((i, cnt))

    if temp != 1:
        pf_cnt.append((temp, 1))
    return pf_cnt


def main():
    ansl = []
    for _ in range(int(input())):
        n = int(input())
        facs = p_factorization_t(n)
        # print(facs)
        if len(facs) == 1:
            p, cnt = facs[0]
            al = []
            for i in range(1, cnt + 1):
                al.append(pow(p, i))
            print(*al)
            print(0)

        ff = []
        pd = {}
        ps = []
        for p, cnt in facs:
            row = []
            for i in range(0, cnt + 1):
                row.append(pow(p, i))
            ff.append(row)
            pd[p] = []
            ps.append(p)

        vals = [1]
        for row in ff:
            new_vals = []
            for v in vals:
                for p in row:
                    new_vals.append(p * v)
                    if p != 1:
                        pd[row[1]].append(v * p)
            vals = new_vals[:]

        if len(facs) >= 3:
            al = []
            for i in range(len(ps)):
                cval = -1
                if i > 0:
                    cval = (ps[i] * ps[i - 1])
                    al.append(cval)
                else:
                    cval = (ps[i] * ps[-1])
                for v in pd[ps[i]]:
                    if v != cval:
                        al.append(v)
            print(*al)
            print(0)

        elif len(facs) == 2:
            al = []
            for i in range(len(ps)):
                cval = -1
                if i > 0:
                    cval = (ps[i] * ps[i - 1])
                    al.append(cval)
                else:
                    cval = (ps[i] * ps[-1])
                for v in pd[ps[i]]:
                    if v != cval:
                        al.append(v)
            print(*al)
            if facs[0][1] == 1 and facs[1][1] == 1:
                print(1)
            else:
                print(0)

        # elif len(facs) == 2:


def __starting_point():
    main()


__starting_point()
