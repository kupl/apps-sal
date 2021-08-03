s = int(input())
S = [str(s)]
i = 1
while True:
    if s % 2 == 0:
        i += 1
        s = s // 2
        S.append(str(s))
        if S.count(str(s)) == 2:
            print(i)
            return
    else:
        i += 1
        s = int(3 * s + 1)
        S.append(str(s))
        if S.count(str(s)) == 2:
            print(i)
            return
pass
