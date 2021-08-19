(x, y, z) = list(map(int, input().split()))
if x == y and x != z:
    print('Yes')
elif x == z and x != y:
    print('Yes')
elif y == z and x != y:
    print('Yes')
else:
    print('No')
