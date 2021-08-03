N = int(input())
lsa = list(map(int, input().split()))
lsb = []
joker = 0
for i in lsa:
    if i >= 1 and i <= 399:
        lsb.append('1')
    elif i >= 400 and i <= 799:
        lsb.append('2')
    elif i >= 800 and i <= 1199:
        lsb.append('3')
    elif i >= 1200 and i <= 1599:
        lsb.append('4')
    elif i >= 1600 and i <= 1999:
        lsb.append('5')
    elif i >= 2000 and i <= 2399:
        lsb.append('6')
    elif i >= 2400 and i <= 2799:
        lsb.append('7')
    elif i >= 2800 and i <= 3199:
        lsb.append('8')
    elif i >= 3200:
        joker += 1
s1 = len(set(lsb))
s2 = s1 + joker
print(max(s1, 1), s2)
