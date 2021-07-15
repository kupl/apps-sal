def fight(k1, k2):
    l = k1.pop(0)
    r = k2.pop(0)
    if l < r:
        k2.extend([l, r])
    else:
        k1.extend([r, l])


n = int(input())
k1 = list(map(int, input().split()))
k1.pop(0)
k2 = list(map(int, input().split()))
k2.pop(0)

combs = set()
fights = 0
while k1 and k2:
    topcomb = (''.join(map(str, k1)), ''.join(map(str, k2)))
    if topcomb in combs:
#        print(fights)
        fights = -1
        break
    combs.add(topcomb)
    fight(k1, k2)
    fights += 1


print(fights, end=' ')
if fights > -1:
    print(1 if k1 else 2)
