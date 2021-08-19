(n, m) = list(map(int, input().split(' ')))
i = 0
while i < n:
    print('#' * m)
    if i != n - 1:
        if i / 2 % 2 == 0:
            print('.' * (m - 1) + '#')
        else:
            print('#' + '.' * (m - 1))
    i += 2
