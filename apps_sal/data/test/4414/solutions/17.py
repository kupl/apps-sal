q = int(input())

for __ in [0]*q:
    a,b,n,s = map(int,input().split())
    xx = min(s//n,a)
    s -= xx*n
    if s <= b:
        print('YES')
    else:
        print('NO')
