def main():
    n = int(input())
    a = [list([int(x) - 1 for x in input().split()]) for _ in range(n)]
    for i in range(n):
        a[i].reverse()
    s = set()

    def check(i, s):
        if len(a[i]) == 0:
            return
        j = a[i][-1]
        if len(a[j]) == 0:
            return
        if a[j][-1] == i:
            if i < j:
                s.add((i, j))
            else:
                s.add((j, i))

    for i in range(n):
        check(i, s)
    day = 0
    while s:
        day += 1
        prevS = set()
        s, prevS = prevS, s
        for p in prevS:
            i = p[0]
            j = p[1]
            a[i].pop()
            a[j].pop()
        for p in prevS:
            i = p[0]
            j = p[1]
            check(i, s)
            check(j, s)

    for i in range(n):
        if len(a[i]):
            print((-1))
            return
    print(day)
    return


main()
