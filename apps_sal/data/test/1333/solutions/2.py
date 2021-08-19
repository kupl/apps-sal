(n, m) = list(map(int, input().split(' ')))
f = 0
for l in range(n):
    if l % 2 == 0:
        print('#' * m)
        f = 1 if f == 0 else 0
    elif f == 1:
        print('.' * (m - 1) + '#')
    else:
        print('#' + '.' * (m - 1))
