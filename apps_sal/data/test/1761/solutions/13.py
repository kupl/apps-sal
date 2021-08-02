def a():
    n = int(input())
    a = [input() for _ in range(n)]
    s = input()
    j = s.find('<')
    i = s.find('3', j)
    for x in a:
        j = i + 1
        for y in x:
            j = s.find(y, j) + 1
            if j == 0:
                print('no')
                return
        j = s.find('<', j)
        i = s.find('3', j)
        if not 0 <= j < i:
            print('no')
            return
    print('yes')


a()
