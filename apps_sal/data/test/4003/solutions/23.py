def main():
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    j = n - 1
    last = -1
    anz = []
    stop = False
    while i != j:
        if a[i] == a[j]:
            stop = True
            break
        if a[i] < a[j]:
            if a[i] > last:
                last = a[i]
                i += 1
                anz.append('L')
            elif a[j] > last:
                last = a[j]
                j -= 1
                anz.append('R')
            else:
                break
        elif a[j] > last:
            last = a[j]
            j -= 1
            anz.append('R')
        elif a[i] > last:
            last = a[i]
            i += 1
            anz.append('L')
        else:
            break
    if i == j and a[i] > last:
        anz.append('R')
    if stop:
        l = []
        r = []
        i1 = i
        last1 = last
        while last1 < a[i] and i != j:
            last1 = a[i]
            i += 1
            l.append('L')
        while last < a[j] and i1 != j:
            last = a[j]
            j -= 1
            r.append('R')
        if len(l) > len(r):
            print(len(anz) + len(l))
            for elem in anz:
                print(elem, end='')
            for elem in l:
                print(elem, end='')
        else:
            print(len(r) + len(anz))
            for elem in anz:
                print(elem, end='')
            for elem in r:
                print(elem, end='')
    else:
        print(len(anz))
        for elem in anz:
            print(elem, end='')


main()
