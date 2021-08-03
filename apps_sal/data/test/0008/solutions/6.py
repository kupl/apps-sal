l = input().split()
if l[0] == l[1] and l[1] == l[2]:
    print(0)
    return


def shuntsu(li):
    li.sort()
    return li[0][1] == li[1][1] and li[1][1] == li[2][1] and int(li[1][0]) == int(li[0][0]) + 1 and int(li[2][0]) == int(li[1][0]) + 1


if shuntsu(l):
    print(0)
    return
for k in l:
    if len([x for x in l if x == k]) > 1:
        print(1)
        return
    if len([x for x in l if x[1] == k[1] and int(x[0]) == int(k[0]) + 1]) != 0:
        print(1)
        return
    if len([x for x in l if x[1] == k[1] and int(x[0]) == int(k[0]) + 2]) != 0:
        print(1)
        return
print(2)
