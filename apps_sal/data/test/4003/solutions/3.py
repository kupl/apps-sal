n = int(input())
l = [*map(int, input().split())]
prev = 0
res = []
while l:
    if l[0] == l[-1]:
        if prev >= l[0]:
            break
        if len(l) <= 2:
            res.append('L')
            break
        (c0, c1) = ([], [])
        p = prev
        for e in l:
            if p < e:
                c0.append('L')
                p = e
            else:
                break
        p = prev
        for e in l[::-1]:
            if p < e:
                c1.append('R')
                p = e
            else:
                break
        if len(c0) <= len(c1):
            res += c1
        else:
            res += c0
        break
    elif prev < l[0] and (l[0] < l[-1] or prev >= l[-1]):
        i = 0
        res.append('L')
    elif prev < l[-1]:
        i = -1
        res.append('R')
    else:
        break
    prev = l[i]
    del l[i]
print(len(res))
print(''.join(res))
