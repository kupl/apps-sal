q=list(map(int,input().split()))
q.sort()
if (1 in q)|(q.count(2)>=2)|(q.count(3)==3)|(q==[2,4,4]):
    print('YES')
else:
    print('NO')

