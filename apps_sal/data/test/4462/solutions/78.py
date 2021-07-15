_ = input()
a = [int(x) for x in input().split()]

odd, m4, m2 = 0, 0, 0
for i in a:
    if i % 2 != 0:
        odd += 1
    elif i % 4 == 0:
        m4 += 1
    else:
        m2 = 1
else:
    if odd + m2 - 1 <= m4:
        print("Yes")
    else:
        print("No")
