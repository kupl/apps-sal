s = int(input())

max_ = 1000000
chk = [0]*max_
a = s
i = 1
while i <= max_:
    if chk[a] == 0:
        chk[a] += 1
    else:
        print(i)
        return
    if a%2 == 0:
        a = int(a/2)
    else:
        a = 3*a + 1
    i += 1

