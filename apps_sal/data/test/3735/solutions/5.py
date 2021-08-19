n = int(input())
sa = '0'


def comp(k):
    a = int(k)
    b = n - a
    return b


while comp(sa) >= 0:
    if comp(sa + '9') >= 0:
        sa += '9'
    else:
        break
print(sum((int(h) for h in sa + str(comp(sa)))))
