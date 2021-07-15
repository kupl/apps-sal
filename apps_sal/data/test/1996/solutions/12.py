n = int(input())
l1 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'h', 'w', 'y', 'x', 'z', 'v'}
for i in range(n - 1):
    l = list(input())
    if l[0] == '.':
        l = set(l[2:])
        l1 -= l
    elif l[0] == '!':
        l = set(l[2:])
        l1 &= l
    else:
        l1 -= set(l[2])
    if len(l1) == 1:
        q = 0
        for k in range(n - i - 2):
            l = list(input())
            if l[0] != '.':
                q += 1
        print(q)
        break
if len(l1) > 1:
    print(0)

