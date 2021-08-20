array1 = [1, 3, 5, 7, 8, 10, 12]
array2 = [4, 6, 9, 11]
array3 = [2]
(x, y) = map(int, input().split())
if x in array1 and y in array1 or (x in array2 and y in array2) or (x in array3 and y in array3):
    print('Yes')
else:
    print('No')
