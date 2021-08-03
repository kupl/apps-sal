a, b, c = map(int, input().split())
if (a == b or b == c or c == a):
    if a == b == c:
        print('No')
    else:
        print('Yes')
else:
    print('No')
