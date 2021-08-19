a = input().split()
n = int(a[0])
m = int(a[1])
for i in range(n):
    if i % 2 == 0:
        print('#' * m)
    elif i % 4 == 3:
        s = '#' + '.' * (m - 1)
        print(s)
    else:
        s = '.' * (m - 1) + '#'
        print(s)
