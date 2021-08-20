t = int(input())
for i in range(t):
    (a, b, c) = sorted([int(x) for x in input().split()])
    if a + b < c - 1:
        print('No')
    else:
        print('Yes')
