x, y = map(int, input().split())
A = set([1, 3, 5, 7, 8, 10, 12])
B = set([4, 6, 9, 11])
if x in A and y in A:
    print('Yes')
elif x in B and y in B:
    print('Yes')
else:
    print('No')
