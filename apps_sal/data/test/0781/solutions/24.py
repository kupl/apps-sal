def foo():
    table = []
    for i in range(8):
        table.append(input())
    w = 'W' * 4
    b = 'B' * 4
    for s in table:
        a1 = s[0:len(s):2]
        a2 = s[1:len(s):2]
        if not (a1 == w and a2 == b or (a1 == b and a2 == w)):
            print('NO')
            return
    print('YES')


foo()
