x, y = map(int, input().split())
s1 = [1, 3, 5, 7, 8, 10, 12]
s2 = [4, 6, 9, 11]
s3 = [2]
if x in s1 and y in s1:
    print('Yes')
elif x in s2 and y in s2:
    print('Yes')
elif x in s3 and y in s3:
    print('Yes')
else:
    print('No')
