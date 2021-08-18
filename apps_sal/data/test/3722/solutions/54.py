def main(n, caa, cab, cba, cbb):
    if n < 4:
        return 1
    ary = [caa, cab, cba, cbb]
    t = 'AB'
    mod = 10**9 + 7
    if ary[0] == 'A' and ary[1] == 'A':
        return 1
    if ary[1] == 'B' and ary[3] == 'B':
        return 1
    elif ary == ['A', 'B', 'A', 'A']:
        return pow(2, n - 3, mod)
    elif ary == ['A', 'B', 'B', 'A']:
        dpa = [0] * (n - 2)
        dpb = [0] * (n - 2)
        dpa[0] = 0
        dpb[0] = 1
        for i in range(n - 3):
            dpa[i + 1] += dpb[i]
            dpb[i + 1] += dpa[i] + dpb[i]
            dpa[i + 1] %= mod
            dpb[i + 1] %= mod
        return (dpa[-1] + dpb[-1]) % mod
    elif ary == ['B', 'A', 'A', 'A']:
        dpa = [0] * (n - 2)
        dpb = [0] * (n - 2)
        dpa[0] = 1
        dpb[0] = 1
        for i in range(n - 3):
            dpa[i + 1] += dpa[i] + dpb[i]
            dpb[i + 1] += dpa[i]
            dpa[i + 1] %= mod
            dpb[i + 1] %= mod
        return dpa[-1]
    elif ary == ['B', 'A', 'A', 'B']:
        dpa = [0] * (n - 2)
        dpb = [0] * (n - 2)
        dpa[0] = 1
        dpb[0] = 1
        for i in range(n - 3):
            dpa[i + 1] += dpa[i] + dpb[i]
            dpb[i + 1] += dpa[i]
            dpa[i + 1] %= mod
            dpb[i + 1] %= mod
        return dpa[-1]
    elif ary == ['B', 'A', 'B', 'A']:
        return pow(2, n - 3, mod)
    elif ary == ['B', 'A', 'B', 'B']:
        return pow(2, n - 3, mod)
    elif ary == ['B', 'B', 'A', 'A']:
        return pow(2, n - 3, mod)
    elif ary == ['B', 'B', 'B', 'A']:
        dpa = [0] * (n - 2)
        dpb = [0] * (n - 2)
        dpa[0] = 0
        dpb[0] = 1
        for i in range(n - 3):
            dpa[i + 1] += dpb[i]
            dpb[i + 1] += dpa[i] + dpb[i]
            dpa[i + 1] %= mod
            dpb[i + 1] %= mod
        return (dpa[-1] + dpb[-1]) % mod
    else:
        return ary[5]


n = int(input())
caa = input()
cab = input()
cba = input()
cbb = input()
print(main(n, caa, cab, cba, cbb))
