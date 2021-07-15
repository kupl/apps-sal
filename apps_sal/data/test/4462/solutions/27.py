_ = input()
a = [int(x) for x in input().split()]

odd = []
m4 = []
m2 = 0
for i in a:
    if i % 2 != 0:
        odd.append(i)
    elif i % 4 == 0:
        m4.append(i)
    else:
        m2 = 1
else:
    lodd = len(odd)
    if lodd == 0 or lodd + m2 - 1 <= len(m4):
        print("Yes")
    else:
        print("No")
