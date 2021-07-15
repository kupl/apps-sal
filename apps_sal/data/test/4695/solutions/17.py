x, y = map(int, input().split())
group1 = [1, 3, 5, 7, 8, 10, 12]
group2 = [4, 6, 9, 11]

flag = False
if x in group1 and y in group1:
    flag = True
elif x in group2 and y in group2:
    flag = True
    
if flag:
    print('Yes')
else:
    print('No')
