import sys

n = int(input())

##I = [i for i in range(1, n + 1)]
##
##levi = 0
##desni = len(I) - 1
##
##prvi = set()
##drugi = set()
##
# while desni - levi >= 3:
# prvi.add(I[levi])
# prvi.add(I[desni])
# drugi.add(I[levi+1])
# drugi.add(I[desni-1])
##    levi += 2
##    desni -= 2
##
# if desni - levi == 2:
# prvi.add(I[levi])
# prvi.add(I[levi+1])
# drugi.add(I[desni])
# elif desni - levi == 1:
# prvi.add(I[levi])
# drugi.add(I[levi+1])
# elif desni - levi == 0:
# prvi.add(I[levi])
# else:
# pass
##
##print(abs(sum(prvi) - sum(drugi)))
##print(str(len(prvi)) + ' ' + ' '.join(map(str, prvi)))

vseh = n * (n + 1) // 2

hit = vseh // 2


def posible(hit, n):
    nums = set()
    maks = n
    while hit > 0:
        if maks > hit:
            maks = hit
        hit -= maks
        nums.add(maks)
        maks -= 1
        if maks <= 0:
            break
    return nums


# print(vseh)
for k in range(5):
    A = posible(hit - k, n)
    x = vseh - sum(A)
    print(abs(x - sum(A)))
    print(str(len(A)) + ' ' + ' '.join(map(str, A)))
    return
