t = int(input())
for i in range(t):
    (a, b, c) = map(int, input().split())
    if 2 * max(a, b, c) - 1 > a + b + c:
        print('No')
    else:
        print('Yes')
