def check(a, b):
    if min(a) < min(b) < max(a) < max(b) or min(b) < min(a) < max(b) < max(a):
        return True
    else:
        return False


lo = False
n = int(input())
l = list(map(int, input().split()))
coppie = []
for cont in range(0, n - 1):
    coppie.append(list((l[cont], l[cont + 1])))
for c in range(0, len(coppie) - 1):
    for d in range(c + 1, len(coppie)):
        if check(coppie[c], coppie[d]):
            print('yes')
            lo = True
            break
    if lo:
        break
if lo is False:
    print('no')
