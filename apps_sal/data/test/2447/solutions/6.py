q = int(input())
for ii in range(q):
    s = input()
    n = len(s)
    wyn = 5298528589245892
    wyn = min(wyn, s.count('0'))
    wyn = min(wyn, s.count('1'))
    cyk = s.count('0')
    for i in range(n):
        if s[i] == '1':
            cyk += 1
        else:
            cyk -= 1
        wyn = min(wyn, cyk)
    cyk = s.count('1')
    for i in range(n):
        if s[i] == '0':
            cyk += 1
        else:
            cyk -= 1
        wyn = min(wyn, cyk)
    print(wyn)
