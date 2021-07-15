def mi():
    return list(map(int, input().split()))
'''
5
2 4 2
5 10 4
3 10 1
1 2 3
4 6 5
'''

for _ in range(int(input())):
    l,r,d = mi()
    nl=d
    nr=r-r%d
    nr+=d

    if nl<l:
        print (nl)
    else:
        print (nr)

