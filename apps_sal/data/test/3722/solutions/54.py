def main(n, caa, cab, cba, cbb):
    if n < 4: return 1
    ary = [caa, cab, cba, cbb]
    t = 'AB'
    mod = 10**9 + 7
    if ary[0] == 'A' and ary[1] == 'A':
        return 1
    if ary[1] == 'B' and ary[3] == 'B':
        return 1
    # elif ary==['A','A','A','A']:
    # elif ary==['A','A','A','B']:
    # elif ary==['A','A','B','A']:
    # elif ary==['A','A','B','B']:
    elif ary == ['A', 'B', 'A', 'A']:  # 先頭はA、末尾はB。xxxの部分は任意。ABxxxxxxB
        return pow(2, n - 3, mod)
    # elif ary==['A','B','A','B']:
    elif ary == ['A', 'B', 'B', 'A']:  # 先頭はA、末尾はB。xxxの部分でAは連続しない。ABxxxxxxxB
        dpa = [0] * (n - 2)  # dpa[i]:i+2文字目がa
        dpb = [0] * (n - 2)  # dpb[i]:i+2文字目がb
        dpa[0] = 0
        dpb[0] = 1
        for i in range(n - 3):
            dpa[i + 1] += dpb[i]
            dpb[i + 1] += dpa[i] + dpb[i]
            dpa[i + 1] %= mod
            dpb[i + 1] %= mod
        return (dpa[-1] + dpb[-1]) % mod
    # elif ary==['A','B','B','B']:
    elif ary == ['B', 'A', 'A', 'A']:  # 先頭はA、末尾はB。xxxの部分でBは連続しない。AxxxxxxxAB
        dpa = [0] * (n - 2)  # dpa[i]:i+2文字目がa
        dpb = [0] * (n - 2)  # dpb[i]:i+2文字目がb
        dpa[0] = 1
        dpb[0] = 1
        for i in range(n - 3):
            dpa[i + 1] += dpa[i] + dpb[i]
            dpb[i + 1] += dpa[i]
            dpa[i + 1] %= mod
            dpb[i + 1] %= mod
        return dpa[-1]
    elif ary == ['B', 'A', 'A', 'B']:  # 先頭はA、末尾はB。xxxの部分は任意。ABxxxxxxxB
        dpa = [0] * (n - 2)  # dpa[i]:i+2文字目がa
        dpb = [0] * (n - 2)  # dpb[i]:i+2文字目がb
        dpa[0] = 1
        dpb[0] = 1
        for i in range(n - 3):
            dpa[i + 1] += dpa[i] + dpb[i]
            dpb[i + 1] += dpa[i]
            dpa[i + 1] %= mod
            dpb[i + 1] %= mod
        return dpa[-1]
    elif ary == ['B', 'A', 'B', 'A']:  # 先頭はA、末尾はB。xxxの部分は任意。AxxxxxxxAB
        return pow(2, n - 3, mod)
    elif ary == ['B', 'A', 'B', 'B']:
        return pow(2, n - 3, mod)
    elif ary == ['B', 'B', 'A', 'A']:  # 先頭はA、末尾はB。xxxの部分は任意。ABxxxxxxxB
        return pow(2, n - 3, mod)
    # elif ary==['B','B','A','B']:
    elif ary == ['B', 'B', 'B', 'A']:  # 先頭はA、末尾はB。xxxの部分でAは連続しない。ABxxxxxxxB
        dpa = [0] * (n - 2)  # dpa[i]:i+2文字目がa
        dpb = [0] * (n - 2)  # dpb[i]:i+2文字目がb
        dpa[0] = 0
        dpb[0] = 1
        for i in range(n - 3):
            dpa[i + 1] += dpb[i]
            dpb[i + 1] += dpa[i] + dpb[i]
            dpa[i + 1] %= mod
            dpb[i + 1] %= mod
        return (dpa[-1] + dpb[-1]) % mod
    # elif ary==['B','B','B','B']:
    else:
        return ary[5]


n = int(input())
caa = input()
cab = input()
cba = input()
cbb = input()
print(main(n, caa, cab, cba, cbb))
