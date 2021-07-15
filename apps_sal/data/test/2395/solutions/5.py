from math import inf
t = int(input())
for q in range(t):
    tt = input()
    s = "01" * len(tt)
    one = False
    zero = False
    for i in tt:
        if i == '0':
            zero = True
        else:
            one = True
    if not one or not zero:
        print(tt)
    else:
        print(s)

