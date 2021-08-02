a, b, c = map(int, input().split())
l = [a, b, c]

if len(set(l)) == 2:
    print('Yes')
else:
    print('No')
