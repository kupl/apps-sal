data_1 =[1,3,5,7,8,10,12]
data_2 =[4,6,9,11]
x,y = map(int,input().split())
if x in data_1 and y in data_1:
    print('Yes')
elif x in data_2 and y in data_2:
    print('Yes')
else:
    print('No')
