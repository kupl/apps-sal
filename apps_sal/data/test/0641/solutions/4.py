ch = str(input())
n = len(ch)
t = ch[n - 1]
e = ch.index(' ')
m = int(ch[:e])
if t == 'k':
    if m == 5 or m == 6:
        print(53)
    else:
        print(52)
elif m <= 29:
    print(12)
elif m == 30:
    print(11)
elif m == 31:
    print(7)
