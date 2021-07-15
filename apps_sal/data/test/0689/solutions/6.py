for _ in range(int(input())):
    n = int(input())
    d = dict()
    for i in range(n):
        for i in input():
            d[i] = d.get(i,0)+1
    s = 0
    for i,j in list(d.items()):
        if d[i]%n!=0:
            s+=1
            break
    if s==0:
        print('YES')
    else:
        print('NO')

