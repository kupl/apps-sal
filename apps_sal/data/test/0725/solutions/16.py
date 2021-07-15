n, m = list(map(int, input().split(' ')))
color = ['B', 'W', 'G']
for i in range(n):
    x = input().split(' ')
    for i in x:
        if i not in color:
            print('#Color')
            return
print('#Black&White')

