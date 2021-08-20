(x, y) = list(map(int, input().split()))
g1 = [1, 3, 5, 7, 8, 10, 12]
g2 = [4, 6, 9, 11]
g3 = [2]
if x in g1 and y in g1:
    print('Yes')
elif x in g2 and y in g2:
    print('Yes')
elif x in g3 and y in g3:
    print('Yes')
else:
    print('No')
