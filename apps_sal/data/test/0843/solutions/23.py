def main():
    n = int(input())
    d = input()
    l = [int(c) for c in input().split()]
    visited = {0}
    i = 0
    while 0 <= i < n:
        di, li = d[i], l[i]
        i = i + li if di == '>' else i - li
        if i in visited:
            print('INFINITE')
            return
        visited.add(i)

    print('FINITE')
        

def __starting_point():
    main()

__starting_point()
