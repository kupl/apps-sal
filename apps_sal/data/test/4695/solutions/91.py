x, y = map(int, input().split())

gr1=[1,3,5,7,8,10,12]
gr2=[4,6,9,11]
gr3=[2]

if x in gr1 and y in gr1:
    print('Yes')
elif x in gr2 and y in gr2:
    print('Yes')
elif x in gr3 and y in gr3:
    print('Yes')
else:
    print('No')
