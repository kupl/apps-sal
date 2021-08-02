G1 = [1, 3, 5, 7, 8, 10, 12]
G2 = [4, 6, 9, 11]
x, y = map(int, input().split())

if x in G1 and y in G1:
    print('Yes')
elif x in G2 and y in G2:
    print('Yes')
else:
    print('No')
