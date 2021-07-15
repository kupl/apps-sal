n = int( input() )

L = []

m = {}
names = []

for i in range( n ):
    a = input().split()

    name = a[0]
    names.append( a[0] )

    a = a[2:]

    if name not in m:
        m[ name ] = []

    for j in a:
        m[ name ].append( j )

names = set( names )

for i in names:

    #print( i )

    a = list( set(m[i] ) )
    #print( a )

    good = [True] * len(a)

    for j in range( len(a) ):
        for k in range( len(a) ):
            if j != k:
                if a[k].endswith( a[j] ):
                    good[j] = False
                    break

    ok = False
    cnt = 0
    for j in range( len(a) ):
        if good[j] == True:
            cnt += 1
            ok = True

    if ok == False:
        continue

    out = i + " " + str(cnt)

    for j in range( len(a) ):
        if good[j]:
            out += " " + a[j]

    L.append( out )

print( len(L) )
for i in L:
    print( i )


return

