a = int(input())
for i in range(a):
    (x, y) = list(map(int, input().split()))
    (r, s) = list(map(int, input().split()))
    if x == s and y + r == s:
        print('Yes')
    elif x == r and y + s == x:
        print('Yes')
    elif y == s and x + r == y:
        print('Yes')
    elif y == r and x + s == y:
        print('Yes')
    else:
        print('No')
