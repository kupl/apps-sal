try:
    s = input()
    l_a = []
    l_b = []
    l_c = []
    for i in range(len(s)):
        if s[i] == 'a':
            l_a.append(i)
    for i in range(len(s)):
        if s[i] == 'b':
            l_b.append(i)
    for i in range(len(s)):
        if s[i] == 'c':
            l_c.append(i)
    maxi = 0
    for i in l_a:
        for j in l_c:
            maxi = max(maxi, abs(i - j))
    for i in l_b:
        for j in l_c:
            maxi = max(maxi, abs(i - j))
    for i in l_a:
        for j in l_b:
            maxi = max(maxi, abs(i - j))
    print(maxi)
except:
    pass
