a,b = list(map(int,input().split()))

li = [2,3,4,5,6,7,8,9,10,11,12,13,1]

a1 = li.index(a)
b1 = li.index(b)

if a1 > b1:
    print('Alice')
elif a1 == b1:
    print('Draw')
else:
    print('Bob')

