for _ in range(int(input())):
    s = input()
    pref = []
    cur = 0
    for i in s:
        if i == '+':
            cur += 1
        else:
            cur -= 1
        pref.append(cur)
    (res, mn) = (0, 0)
    for i in range(len(pref)):
        if pref[i] < mn:
            mn = pref[i]
            res += i + 1
    print(res + len(s))
