x,y = map(int,input().split())

grp1=[1,3,5,7,8,10,12]
grp2=[4,6,9,11]

if x in grp1 and y in grp1: print('Yes')
elif x in grp2 and y in grp2: print('Yes')
else: print('No')
