(a, b, c, n) = map(int, input().split())
if abs(c - a) <= n:
    print('Yes')
elif abs(c - b) <= n and abs(b - a) <= n:
    print('Yes')
else:
    print('No')
