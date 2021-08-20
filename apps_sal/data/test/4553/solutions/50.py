(a, b) = map(int, input().split())
l = input().split('-')
if len(l[0]) == a and len(l[1]) == b:
    print('Yes')
else:
    print('No')
