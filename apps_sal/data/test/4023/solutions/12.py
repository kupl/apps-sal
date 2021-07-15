def f():
    b = [a[0]]
    for e in a[1:]:
        if b != []:
            if e > b[-1]:
                print('NO')
                return
            elif e == b[-1]:
                b.pop()
            else:
                b.append(e)
        else:
            b.append(e)

    if len(b)==0:
        print('YES')

    else:
        if len(set(b))==1 and b[0]==max(a):
            print('YES')
        else:
            print('NO')

n=int(input())
a=[int(i) for i in input().split()]


f()
