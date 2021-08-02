n = int(input())
for i in range(n):
    s = list(input())
    s.append(0)
    dan = []
    counter = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            dan.append((s[i - 1], counter))
            counter = 1
        else:
            counter += 1
    t = list(input())
    t.append(0)
    j = 0
    lena = len(dan)
    counter = 1
    for i in range(1, len(t)):
        if t[i] != t[i - 1]:
            if j >= lena:
                print('NO')
                break
            if t[i - 1] == dan[j][0] and counter >= dan[j][1]:
                j += 1
                counter = 1
            else:
                print('NO')
                break
        else:
            counter += 1
    else:
        if j == lena:
            print('YES')
        else:
            print('NO')
