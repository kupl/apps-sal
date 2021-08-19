def check(n):
    if n == 'a':
        if len(a) > 0:
            check(a.pop())
        else:
            print('A')
    elif n == 'b':
        if len(b) > 0:
            check(b.pop())
        else:
            print('B')
    elif n == 'c':
        if len(c) > 0:
            check(c.pop())
        else:
            print('C')


(a, b, c) = [[*input()][::-1] for _ in range(3)]
check(a.pop())
