raw = input()
raw = list(raw)
raw = [int(x) for x in raw]
flag = 0
lst = []
for x in raw:
    if x % 2 == 0:
        flag = 1
        lst.append(x)
if flag == 1:
    lst = sorted(lst)
    l = raw[-1]
    if lst[0] > l:
        for x in reversed(raw):
            if x % 2 == 0:
                s = x
                break
        i = [i for (i, x) in enumerate(raw) if x == s]
        raw[i[-1]] = l
        raw[-1] = s
        raw = [str(x) for x in raw]
        print(''.join(raw))
    else:
        for x in raw:
            if x % 2 == 0:
                if x < l:
                    s = x
                    break
        raw[-1] = s
        raw[raw.index(s)] = l
        raw = [str(x) for x in raw]
        print(''.join(raw))
else:
    print(-1)
