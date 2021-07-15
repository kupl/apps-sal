for _ in range(int(input())):
    s = input()
    res = s.count('0')
    i = 0
    while i < len(s) and s[i] == '0':
        res -= 1
        i += 1
    j = len(s) - 1
    while j > i and s[j] == '0':
        res -= 1
        j -= 1
    print(res)

