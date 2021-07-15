n,m=[int(x) for x in input().split()]
pairs=[]
for i in range(m):
    a=([int(x) for x in input().split()])
    pairs.append(a)
x,y=pairs[0][0],pairs[0][1]
for item in pairs:
    if item[0]!=x and item[0]!=y and item[1]!=x and item[1]!=y:
        a,b,c,d=x,y,item[0],item[1]
        break
else:
    a,b,c,d=x,y,x,y
for x,y in (a,b),(a,c),(b,d),(c,d),(a,d),(b,c):
    for item in pairs:
        if item[0]!=x and item[1]!=x and item[0]!=y and item[1]!=y:
            break
    else:
        print('YES')
        break
else:
    print('NO')

