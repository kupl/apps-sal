def ain():
    return list(map( int, input().split() ))



# for _ in range( int(input()) ):
# n = int(input())
# python3 g.py

for _ in range( int(input()) ):
    s = input()
    t = input()
    p = input()
    fl = False
    i = 0
    for x in s:
        while i<len(t) and t[i] != x:
            i+=1
        if i == len(t):
            fl = True
            break
        i+=1
    if fl:
        print('NO')
    else:
        for x in t:
            if s.count(x) + p.count(x) < t.count(x):
                #print( x , s.count(x), p.count(x) , t.count(x)  )
                print('NO')
                fl = True
                break
        if not fl:
            print('YES')


