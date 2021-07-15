t = int(input())
for case in range(t):
    a, b = list(map(int, input().split()))
    c, d = list(map(int, input().split()))
    if a == c and b + d == a:
        print('Yes')
    elif b == d and a + c == b:
        print('Yes')
    elif a == d and b + c == a:
        print('Yes')
    elif b == c and a + d == b:
        print('Yes')
    else:
        print('No')
