t = int(input())
for i in range(t):
    s = input()
    x = len(s)
    (f1, f2, fl3) = (False, False, False)
    j = 0
    cnt = 0
    res = []
    colo = 0
    while j < x:
        if j + 2 <= x:
            if s[j:j + 3] == 'two':
                if j + 3 < x:
                    if s[j + 3] == 'o':
                        res.append(j + 2)
                        j += 2
                    else:
                        res.append(j + 3)
                        j += 3
                else:
                    res.append(j + 3)
                    j += 3
                cnt += 1
            elif s[j:j + 3] == 'one':
                if colo > 0:
                    res.append(j + 2)
                    colo = 0
                else:
                    res.append(j + 1)
                cnt += 1
                j += 3
            else:
                if s[j] == 'o':
                    colo += 1
                j += 1
        else:
            break
    print(cnt)
    print(*res)
