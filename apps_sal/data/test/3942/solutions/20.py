def __starting_point():
    s = input()
    ans = []
    (cnt, key, tmp, new) = (0, True, 0, 0)
    for e in s:
        if e == '(':
            cnt += 1
            new += 1
        elif e == ')':
            cnt -= 1
            if new > 0:
                new -= 1
            if cnt < 0:
                key = False
                break
        else:
            if cnt == 0:
                key = False
                break
            new = 0
            ans.append(1)
            cnt -= 1
            tmp = cnt
    if not key or tmp < cnt or new > 0:
        print(-1)
    else:
        ans[-1] += cnt
        for e in ans:
            print(e)


__starting_point()
