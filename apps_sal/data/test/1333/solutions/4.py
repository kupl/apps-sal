s = input().split()
(c, r) = (int(s[0]), int(s[1]))
s = '#' * r
k = '.' * (r - 1)
for i in range(1, c + 1):
    if i % 2 == 1:
        print(s)
    elif i % 4 == 0:
        print('#' + k)
    else:
        print(k + '#')
