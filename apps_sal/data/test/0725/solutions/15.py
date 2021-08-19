(n, m) = list(map(int, input().split()))
flag = True
for i in range(n):
    a = input().split()
    for j in a:
        if j == 'C' or j == 'M' or j == 'Y':
            flag = False
if flag:
    print('#Black&White')
else:
    print('#Color')
