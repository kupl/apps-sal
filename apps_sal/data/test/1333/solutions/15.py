
m, n = list(map(int, input().split()))

for i in range(m):
    if i % 4 == 0:
        print('#' * n)
    elif i % 4 == 1:
        print('.' * (n - 1) + '#')
    elif i % 4 == 2:
        print('#' * n)
    else:
        print('#' + '.' * (n - 1))
