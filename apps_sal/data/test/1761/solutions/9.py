def f():
    n = int(input())
    t = [input() for i in range(n)]
    p = input()
    j = 0
    for i in range(n):
        for c in '<3':
            j = p.find(c, j) + 1
            if j == 0:
                return 'no'
        for c in t[i]:
            j = p.find(c, j) + 1
            if j == 0:
                return 'no'
    for c in '<3':
        j = p.find(c, j) + 1
        if j == 0:
            return 'no'
    return 'yes'


print(f())
