n = int(input())
for i in ' ' * n:
    (a, b, c) = map(int, input().split())
    if a + b + 1 < c or a + c + 1 < b or b + c + 1 < a:
        print('No')
    else:
        print('Yes')
