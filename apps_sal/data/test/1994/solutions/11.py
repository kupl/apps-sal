def z_advanced(s):
    """An advanced computation of Z-values of a string."""
    Z = [0] * len(s)
    Z[0] = len(s)
    rt = 0
    lt = 0
    for k in range(1, len(s)):
        if k > rt:
            n = 0
            while n + k < len(s) and s[n] == s[n + k]:
                n += 1
            Z[k] = n
            if n > 0:
                lt = k
                rt = k + n - 1
        else:
            p = k - lt
            right_part_len = rt - k + 1
            if Z[p] < right_part_len:
                Z[k] = Z[p]
            else:
                i = rt + 1
                while i < len(s) and s[i] == s[i - k]:
                    i += 1
                Z[k] = i - k
                lt = k
                rt = i - 1
    return Z


def kmptab(s):
    tab = [0] * len(s)
    i = 1
    j = 0
    while i < len(s):
        if s[i] == s[j]:
            tab[i] = j + 1
            i += 1
            j += 1
        elif j != 0:
            j = tab[j - 1]
        else:
            i += 1
    return tab


def __starting_point():
    s = input()
    tab = kmptab(s)
    my_set = set()
    i = len(s)
    while i != 0:
        my_set.add(i)
        i = tab[i - 1]
    V = []
    dict = {}
    for i in my_set:
        V.append(i)
        dict[i] = 0
    Z = z_advanced(s)
    v = []
    V.sort()
    my_tab = [0] * (len(s) + 1)
    for i in Z:
        my_tab[i] += 1
    somme = 0
    for i in range(len(my_tab) - 1, -1, -1):
        my_tab[i] += somme
        somme = my_tab[i]
    for i in dict:
        dict[i] = my_tab[i]
        v.append((dict[i], i))
    v.sort(key=lambda tup: tup[1])
    print(len(v))
    for i in v:
        print(str(i[1]) + ' ' + str(i[0]))


__starting_point()
