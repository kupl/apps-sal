def search(l, r, pr):
    posl = ''
    fl = True
    while l <= r:
        if sp[l] < sp[r]:
            if sp[l] > pr:
                pr = sp[l]
                l += 1
                posl += 'L'
            elif sp[r] > pr:
                pr = sp[r]
                r -= 1
                posl += 'R'
            else:
                fl = False
        elif sp[l] > sp[r]:
            if sp[r] > pr:
                pr = sp[r]
                r -= 1
                posl += 'R'
            elif sp[l] > pr:
                pr = sp[l]
                l += 1
                posl += 'L'
            else:
                fl = False
        else:
            if sp[l] > pr:
                fst = search(l + 1, r, sp[l]) + 'L'
                sec = search(l, r - 1, sp[r]) + 'R'
                if len(sec) > len(fst):
                    posl += sec
                else:
                    posl += fst
            fl = False
        if not fl:
            break
    return posl


n = int(input())
sp = list(map(int, input().split()))
pr = 0
posl = ''
l = 0
r = n - 1
new = search(l, r, 0)
print(len(new))
print(new)
