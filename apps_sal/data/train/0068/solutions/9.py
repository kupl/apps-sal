for _ in range(int(input())):
    n = int(input())
    s = input()
    a = []
    curr = 1
    g = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:
            curr += 1
        else:
            a.append(curr)
            if curr > 1:
                g += 1
            curr = 1
    if curr > 0:
        if curr > 1:
            g += 1
        a.append(curr)
    # print(a)
    j = 0
    i = 0
    res = 0
    while i < len(a):
        if a[i] > 1:
            res += 1
            i += 1
        else:
            j = max(i + 1, j)
            ch = 0
            while j < len(a):
                if a[j] > 1:
                    a[j] -= 1
                    ch = 1
                    break
                j += 1
            if ch == 1:
                i += 1
                res += 1
            else:
                i += 2
                res += 1
    print(res)
