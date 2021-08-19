(a, b, c) = list(map(int, input().split()))
if (1 <= a <= 100) & (1 <= b <= 100) & (1 <= c <= 100):
    if (a + b == c) | (a == b + c) | (a + c == b):
        print('Yes')
    else:
        print('No')
