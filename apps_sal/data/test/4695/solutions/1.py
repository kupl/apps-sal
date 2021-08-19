lst1 = [4, 6, 9, 11]
lst2 = [2]
lst3 = [1, 3, 5, 7, 8, 10, 12]
(x, y) = map(int, input().split())
if x in lst1 and y in lst1:
    print('Yes')
elif x in lst2 and y in lst2:
    print('Yes')
elif x in lst3 and y in lst3:
    print('Yes')
else:
    print('No')
