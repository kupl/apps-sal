l = list(map(str, input().split()))
if l[2] == 'month':
    if int(l[0]) <= 29:
        print(12)
    if int(l[0]) == 30:
        print(11)
    if int(l[0]) == 31:
        print(7)
else:
    x = int(l[0])
    if x >= 1 and x <= 4 or x == 7:
        print(52)
    if x == 5 or x == 6:
        print(53)
