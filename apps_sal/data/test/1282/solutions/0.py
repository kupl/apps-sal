t = input()[::-1]
i = t.find('F')
if i < 0:
    print(0)
else:
    j = t.find('M', i + 1)
    if j < 0:
        print(0)
    else:
        (s, t) = (0, t[j:t.rfind('M') + 1])
        for k in t:
            if k == 'M':
                s += 1
            else:
                s = max(s - 1, 0)
        print(s + t.count('F') + j - i - 1)
