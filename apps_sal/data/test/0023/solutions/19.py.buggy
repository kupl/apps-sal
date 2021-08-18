a = input()
b = input()
if len(b) > len(a):
    tmp = list(a)
    tmp.sort(reverse=True)
    for i in tmp:
        print(i, end="")
    return
sa = [0] * 10
for i in a:
    sa[int(i)] += 1


def tolow():
    tmp = ""
    for i in range(0, 10):
        tmp += str(i) * sa[i]
    return tmp


def tobig():
    tmp = ""
    for i in range(9, -1, -1):
        tmp += str(i) * sa[i]
    return tmp


nakop = ""
for i in range(len(b)):
    tmp = int(b[i])
    if (sa[tmp] > 0):
        sa[tmp] -= 1
        cur = int(nakop + b[i] + tolow())
        if cur <= int(b):
            nakop += str(b[i])
            continue
        else:
            sa[tmp] += 1
            for j in range(tmp - 1, -1, -1):
                if sa[j]:
                    sa[j] -= 1
                    print(nakop + str(j) + tobig())
                    return
    else:
        for j in range(tmp - 1, -1, -1):
            if sa[j]:
                sa[j] -= 1
                print(nakop + str(j) + tobig())
                return


print(nakop)
