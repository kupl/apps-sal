def mi():
    return map(int, input().split())


'''
4
4
3 2 7 6
3
3 2 6
1
7
7
4 9 2 1 18 3 0
'''
for _ in range(int(input())):
    n = int(input())
    a = list(mi())

    o, e = 0,0
    for i in range(n):
        if i%2:
            if a[i]%2==0:
                o+=1
        else:
            if a[i]%2:
                e+=1
    if o==e:
        print(o)
    else:
        print (-1)
