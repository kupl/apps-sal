x,y=list(map(int,input().split()))
for l in [[1,3,5,7,8,10,12],[4,6,9,11],[2]]:
    if x in l and y in l:
        print('Yes')
        return
print('No')

