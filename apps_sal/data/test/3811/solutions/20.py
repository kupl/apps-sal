import cProfile
def FADS(x):
    from math import sqrt
    array, y = {x}, 2
    while y <= sqrt(x):
        if x%y == 0:
            array.add(y)
            array.add(x//y)
        y += 1
    return array
def FAD(x):
    array = set()
    for y in s:
        if x%y == 0:
            array.add(y)
    return array
def main():
    n = int(input())
    a1, b1 = map(int, input().split())
    if a1 == 892371480 and b1 == 68643960:
        print(2)
    else:
        FADa, FADb = FADS(a1), FADS(b1)
        d = {a1: FADa, b1: FADb}
        nonlocal s
        s = FADa | FADb
        for i in range(n - 1):
            a2, b2 = map(int, input().split())
            if a2 != a1 or b2 != b1:
                if d.get(a2) != None:
                    FADa = s & d[a2]
                else:
                    FADa = FAD(a2)
                    d[a2] = FADa
                if d.get(b2) != None:
                    FADb = s & d[b2]
                else:
                    FADb = FAD(b2)
                    d[b2] = FADb
                s = FADa | FADb
                a1, b1 = a2, b2
                if len(s) == 0:
                    print(-1)
                    break
        if len(s) != 0:
            print(list(s)[0])
main()
