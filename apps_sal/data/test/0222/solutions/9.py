a = int(input())
sa = str(a)
i = 1


def check(sa, si):
    cc = 0
    for i in range(len(sa)):
        if sa[i] == si[cc]:
            cc += 1
        if cc == len(si):
            break
    if cc == len(si):
        return True
    else:
        return False


i = int(a ** 0.5 + 1)
while i > 0:
    if i * i > a:
        i -= 1
        continue
    si = str(i * i)
    T = check(sa, si)
    if T:
        print(len(sa) - len(si))
        quit()
    i -= 1
print(-1)
