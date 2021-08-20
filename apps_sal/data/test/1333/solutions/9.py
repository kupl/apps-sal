(n, m) = tuple((int(x) for x in input().split()))
right = True
while n:
    if n % 2 == 1:
        print('#' * m)
    elif right:
        print('.' * (m - 1), '#', sep='')
        right = False
    else:
        print('#', '.' * (m - 1), sep='')
        right = True
    n -= 1
