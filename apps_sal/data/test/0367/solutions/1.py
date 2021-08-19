from collections import Counter, OrderedDict
try:
    while True:
        s = input()
        count = [0] * 26
        for c in s:
            count[ord(c) - 97] += 1
        odds = []
        for (i, x) in enumerate(count):
            if x & 1:
                odds.append(i)
        j = 0
        for (i, x) in zip(range(25, -1, -1), reversed(count)):
            if x & 1:
                if i == odds[j]:
                    break
                count[odds[j]] += 1
                count[i] -= 1
                j += 1
        a = []
        b = []
        c = ''
        for (i, x) in enumerate(count):
            if x & 1:
                assert not c
                c = chr(i + 97)
            if x > 1:
                t = chr(i + 97) * (x >> 1)
                a.append(t)
                b.append(t)
        print(''.join(a), ''.join(reversed(b)), sep=c)
except EOFError:
    pass
