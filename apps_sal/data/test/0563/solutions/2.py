__author__ = "zabidon"

l, r = map(int, input().split())


def alg_evk(a, b):
    while(a % b):
        b, a = a % b, b

    return b


found = False
for a in range(r + 1)[l:]:
    if found:
        break
    for b in range(r + 1)[l:]:
        if found:
            break
        if alg_evk(a, b) != 1:
            continue
        for c in range(r + 1)[l:]:
            if a < b < c:
                if alg_evk(b, c) == 1 and alg_evk(a, c) != 1:
                    found = True
                    result = (a, b, c)
                    break

if(found):
    print("{} {} {}".format(result[0], result[1], result[2]))
else:
    print(-1)
